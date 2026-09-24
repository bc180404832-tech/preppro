import { loadConfig, saveConfig } from './config.js';

export class AIProviderService {
  constructor() {
    this.config = loadConfig();
  }

  reloadConfig() {
    this.config = loadConfig();
  }

  /**
   * Helper to check if an error is a rate limit or quota error
   */
  isRateLimitError(status, message) {
    if (status === 429) return true;
    const msg = (message || '').toLowerCase();
    return (
      msg.includes('rate limit') ||
      msg.includes('resource_exhausted') ||
      msg.includes('quota') ||
      msg.includes('too many requests') ||
      msg.includes('exceeded') ||
      msg.includes('credits')
    );
  }

  /**
   * Call Google AI Studio (Gemini)
   */
  async callGemini(prompt, systemInstruction = '', modelOverride = null) {
    const apiKey = this.config.gemini.apiKey;
    if (!apiKey) {
      throw new Error('Google AI Studio API key is not configured.');
    }

    const model = modelOverride || this.config.gemini.model || 'gemini-2.5-flash';
    const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;

    const contents = [];
    if (systemInstruction) {
      contents.push({
        role: 'user',
        parts: [{ text: `[System Instruction / Persona]\n${systemInstruction}\n\n[Candidate Task]\n${prompt}` }]
      });
    } else {
      contents.push({
        role: 'user',
        parts: [{ text: prompt }]
      });
    }

    const payload = {
      contents,
      generationConfig: {
        temperature: 0.2,
        maxOutputTokens: 2500
      }
    };

    let response;
    try {
      response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
    } catch (netErr) {
      throw new Error(`Google AI Studio network error: ${netErr.message}`);
    }

    if (!response.ok) {
      let errorBody = '';
      try {
        errorBody = await response.text();
      } catch (e) {
        errorBody = response.statusText;
      }

      if (this.isRateLimitError(response.status, errorBody)) {
        const err = new Error(`Google AI Studio Rate Limit (HTTP ${response.status}): Quota exhausted or rate limited.`);
        err.isRateLimit = true;
        err.provider = 'gemini';
        throw err;
      }
      throw new Error(`Google AI Studio error (${response.status}): ${errorBody}`);
    }

    const data = await response.json();
    const candidate = data.candidates?.[0]?.content?.parts?.[0]?.text;
    if (!candidate) {
      throw new Error('Google AI Studio returned an empty response.');
    }
    return candidate;
  }

  /**
   * Call OpenRouter
   */
  async callOpenRouter(prompt, systemInstruction = '', modelOverride = null) {
    const apiKey = this.config.openrouter.apiKey;
    if (!apiKey) {
      throw new Error('OpenRouter API key is not configured.');
    }

    const model = modelOverride || this.config.openrouter.model || 'google/gemini-2.5-flash';
    const url = 'https://openrouter.ai/api/v1/chat/completions';

    const messages = [];
    if (systemInstruction) {
      messages.push({ role: 'system', content: systemInstruction });
    }
    messages.push({ role: 'user', content: prompt });

    const payload = {
      model,
      messages,
      temperature: 0.2,
      max_tokens: 2500
    };

    let response;
    try {
      response = await fetch(url, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
          'HTTP-Referer': 'https://github.com/bc180404832-tech/preppro',
          'X-Title': 'PrepPro PERN/MERN AI Coach'
        },
        body: JSON.stringify(payload)
      });
    } catch (netErr) {
      throw new Error(`OpenRouter network error: ${netErr.message}`);
    }

    if (!response.ok) {
      let errorBody = '';
      try {
        errorBody = await response.text();
      } catch (e) {
        errorBody = response.statusText;
      }

      if (this.isRateLimitError(response.status, errorBody)) {
        const err = new Error(`OpenRouter Rate Limit (HTTP ${response.status}): Quota or rate limit exceeded.`);
        err.isRateLimit = true;
        err.provider = 'openrouter';
        throw err;
      }
      throw new Error(`OpenRouter error (${response.status}): ${errorBody}`);
    }

    const data = await response.json();
    const choice = data.choices?.[0]?.message?.content;
    if (!choice) {
      throw new Error('OpenRouter returned an empty response.');
    }
    return choice;
  }

  /**
   * Execute AI completion with intelligent rate limit fallback
   * Returns: { text, usedProvider, fallbackTriggered }
   */
  async executeWithFallback(prompt, systemInstruction = '', onNotice = null) {
    this.reloadConfig();
    const primary = this.config.primaryProvider; // 'gemini' | 'openrouter'
    const secondary = primary === 'gemini' ? 'openrouter' : 'gemini';

    const hasPrimaryKey = primary === 'gemini' ? !!this.config.gemini.apiKey : !!this.config.openrouter.apiKey;
    const hasSecondaryKey = secondary === 'gemini' ? !!this.config.gemini.apiKey : !!this.config.openrouter.apiKey;

    // If primary has no key, but secondary does, seamlessly use secondary
    if (!hasPrimaryKey && hasSecondaryKey) {
      if (onNotice) {
        onNotice(`ℹ️ ${primary.toUpperCase()} key not found. Using configured ${secondary.toUpperCase()}...`);
      }
      const text = secondary === 'gemini'
        ? await this.callGemini(prompt, systemInstruction)
        : await this.callOpenRouter(prompt, systemInstruction);
      return { text, usedProvider: secondary, fallbackTriggered: true };
    }

    if (!hasPrimaryKey && !hasSecondaryKey) {
      throw new Error('No API keys configured. Please configure Google AI Studio or OpenRouter API key in Settings.');
    }

    // Try primary first
    try {
      const text = primary === 'gemini'
        ? await this.callGemini(prompt, systemInstruction)
        : await this.callOpenRouter(prompt, systemInstruction);
      return { text, usedProvider: primary, fallbackTriggered: false };
    } catch (err) {
      // If error is rate-limit, and fallback is enabled, and secondary key exists:
      if (err.isRateLimit && this.config.autoFallback && hasSecondaryKey) {
        if (onNotice) {
          onNotice(`⚠️ Rate limit reached on ${primary.toUpperCase()}! Switching automatically to fallback provider ${secondary.toUpperCase()}...`);
        }
        try {
          const text = secondary === 'gemini'
            ? await this.callGemini(prompt, systemInstruction)
            : await this.callOpenRouter(prompt, systemInstruction);
          return { text, usedProvider: secondary, fallbackTriggered: true };
        } catch (secondaryErr) {
          throw new Error(`Both primary (${primary}) and fallback (${secondary}) failed.\nPrimary: ${err.message}\nFallback: ${secondaryErr.message}`);
        }
      }
      throw err;
    }
  }

  /**
   * Test connection to a specific provider
   */
  async testProvider(providerName) {
    const testPrompt = 'Respond with exactly: "OK"';
    if (providerName === 'gemini') {
      const res = await this.callGemini(testPrompt);
      return res.includes('OK') || res.length > 0;
    } else {
      const res = await this.callOpenRouter(testPrompt);
      return res.includes('OK') || res.length > 0;
    }
  }
}

export const aiService = new AIProviderService();
