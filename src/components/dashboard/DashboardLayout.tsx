'use client';

import type { ReactNode } from 'react';

interface DashboardLayoutProps {
  children: ReactNode;
  sidebar?: ReactNode;
}

export function DashboardLayout({ children, sidebar }: DashboardLayoutProps) {
  return (
    <div className="flex h-screen overflow-hidden">
      {sidebar && (
        <aside className="w-64 shrink-0 border-r bg-white" aria-label="Sidebar">
          {sidebar}
        </aside>
      )}
      <main className="flex-1 overflow-y-auto p-6">
        {children}
      </main>
    </div>
  );
}
