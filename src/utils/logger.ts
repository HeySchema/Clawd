type LogLevel = 'debug' | 'info' | 'warn' | 'error';

interface LogEntry {
  level: LogLevel;
  message: string;
  timestamp: string;
  context?: Record<string, unknown>;
}

function formatEntry(level: LogLevel, message: string, context?: Record<string, unknown>): LogEntry {
  return {
    level,
    message,
    timestamp: new Date().toISOString(),
    ...(context && { context }),
  };
}

function log(level: LogLevel, message: string, context?: Record<string, unknown>) {
  if (process.env.NODE_ENV === 'test') return;

  const entry = formatEntry(level, message, context);

  switch (level) {
    case 'debug':
      if (process.env.NODE_ENV === 'development') {
        console.debug(JSON.stringify(entry));
      }
      break;
    case 'info':
      console.info(JSON.stringify(entry));
      break;
    case 'warn':
      console.warn(JSON.stringify(entry));
      break;
    case 'error':
      console.error(JSON.stringify(entry));
      break;
  }
}

export const logger = {
  debug: (message: string, context?: Record<string, unknown>) => log('debug', message, context),
  info: (message: string, context?: Record<string, unknown>) => log('info', message, context),
  warn: (message: string, context?: Record<string, unknown>) => log('warn', message, context),
  error: (message: string, context?: Record<string, unknown>) => log('error', message, context),
};
