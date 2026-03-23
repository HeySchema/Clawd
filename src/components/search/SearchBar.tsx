'use client';

import { useCallback, useState } from 'react';

interface SearchBarProps {
  placeholder?: string;
  onSearch: (query: string) => void;
  debounceMs?: number;
}

export function SearchBar({ placeholder = 'Search…', onSearch, debounceMs = 300 }: SearchBarProps) {
  const [value, setValue] = useState('');

  const handleChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const q = e.target.value;
      setValue(q);
      const timer = setTimeout(() => onSearch(q), debounceMs);
      return () => clearTimeout(timer);
    },
    [onSearch, debounceMs],
  );

  return (
    <div role="search">
      <label htmlFor="search-input" className="sr-only">
        Search
      </label>
      <input
        id="search-input"
        type="search"
        value={value}
        onChange={handleChange}
        placeholder={placeholder}
        aria-label="Search"
        className="w-full rounded border px-3 py-2"
      />
    </div>
  );
}
