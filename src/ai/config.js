import fs from 'fs';
import path from 'path';
import os from 'os';
import dotenv from 'dotenv';

// Load .env if present
dotenv.config({ quiet: true });

const CONFIG_DIR = path.join(os.homedir(), '.preppro');
const CONFIG_FILE = path.join(CONFIG_DIR, 'config.json');

const DEFAULT_CONFIG = {
  primaryProvider: 'gemini', // 'gemini' | 'openrouter'
  autoFallback: true,
  gemini: {
    apiKey: process.env.GEMINI_API_KEY || process.env.GOOGLE_AI_KEY || '',
    model: 'gemini-2.5-flash'
  },
  openrouter: {
    apiKey: process.env.OPENROUTER_API_KEY || '',
    model: 'google/gemini-2.5-flash'
  }
};

/**
 * Loads configuration from file and environment variables
 */
export function loadConfig() {
  let fileConfig = {};
  try {
    if (fs.existsSync(CONFIG_FILE)) {
      const raw = fs.readFileSync(CONFIG_FILE, 'utf-8');
      fileConfig = JSON.parse(raw);
    }
  } catch (err) {
    // If parsing fails, fall back silently to default
  }

  // Environment variables override empty file config
  const geminiKey = fileConfig.gemini?.apiKey || process.env.GEMINI_API_KEY || process.env.GOOGLE_AI_KEY || '';
  const openrouterKey = fileConfig.openrouter?.apiKey || process.env.OPENROUTER_API_KEY || '';

  return {
    primaryProvider: fileConfig.primaryProvider || DEFAULT_CONFIG.primaryProvider,
    autoFallback: fileConfig.autoFallback !== undefined ? fileConfig.autoFallback : true,
    gemini: {
      apiKey: geminiKey,
      model: fileConfig.gemini?.model || DEFAULT_CONFIG.gemini.model
    },
    openrouter: {
      apiKey: openrouterKey,
      model: fileConfig.openrouter?.model || DEFAULT_CONFIG.openrouter.model
    }
  };
}

/**
 * Saves configuration to ~/.preppro/config.json
 */
export function saveConfig(newConfig) {
  try {
    if (!fs.existsSync(CONFIG_DIR)) {
      fs.mkdirSync(CONFIG_DIR, { recursive: true });
    }
    const current = loadConfig();
    const merged = {
      ...current,
      ...newConfig,
      gemini: { ...current.gemini, ...(newConfig.gemini || {}) },
      openrouter: { ...current.openrouter, ...(newConfig.openrouter || {}) }
    };
    fs.writeFileSync(CONFIG_FILE, JSON.stringify(merged, null, 2), 'utf-8');
    return true;
  } catch (err) {
    console.error('Failed to save config:', err.message);
    return false;
  }
}

/**
 * Checks if at least one API key is available
 */
export function hasAnyApiKey() {
  const config = loadConfig();
  return Boolean(config.gemini.apiKey || config.openrouter.apiKey);
}
