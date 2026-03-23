import { describe, it, expect } from 'vitest';
import { formatDate, truncate, slugify, safeJsonParse } from '../../src/utils/helpers';

describe('formatDate', () => {
  it('formats a Date object', () => {
    const result = formatDate(new Date('2024-01-15'), 'en-US');
    expect(result).toBe('January 15, 2024');
  });

  it('formats a date string', () => {
    const result = formatDate('2024-06-01', 'en-US');
    expect(result).toBe('June 1, 2024');
  });
});

describe('truncate', () => {
  it('returns the original string when within limit', () => {
    expect(truncate('hello', 10)).toBe('hello');
  });

  it('truncates and appends ellipsis when over limit', () => {
    expect(truncate('hello world', 8)).toBe('hello...');
  });
});

describe('slugify', () => {
  it('converts a string to a slug', () => {
    expect(slugify('Hello World!')).toBe('hello-world');
  });

  it('handles multiple spaces and special chars', () => {
    expect(slugify('  Foo   Bar--Baz  ')).toBe('foo-bar-baz');
  });
});

describe('safeJsonParse', () => {
  it('parses valid JSON', () => {
    expect(safeJsonParse<{ a: number }>('{"a":1}')).toEqual({ a: 1 });
  });

  it('returns null for invalid JSON', () => {
    expect(safeJsonParse('not json')).toBeNull();
  });
});
