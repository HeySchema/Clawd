export type { Database } from './database';

// ─── Common utility types ────────────────────────────────────────────────────

export type Nullable<T> = T | null;
export type Optional<T> = T | undefined;
export type AsyncFn<TArgs extends unknown[], TReturn> = (...args: TArgs) => Promise<TReturn>;

// ─── API response envelope ───────────────────────────────────────────────────

export interface ApiResponseType<T> {
  data: T;
  error: null;
}

export interface ApiErrorType {
  data: null;
  error: {
    message: string;
    code: string;
    statusCode: number;
  };
}

export type ApiResult<T> = ApiResponseType<T> | ApiErrorType;

// ─── Pagination ──────────────────────────────────────────────────────────────

export interface PaginatedResultType<T> {
  items: T[];
  total: number;
  page: number;
  limit: number;
  hasNextPage: boolean;
  hasPreviousPage: boolean;
}

// ─── User ────────────────────────────────────────────────────────────────────

export interface UserType {
  id: string;
  email: string;
  name: string | null;
  avatarUrl: string | null;
  createdAt: Date;
  updatedAt: Date;
}

export interface UserProfileProps {
  user: UserType;
  onEdit?: () => void;
}

// ─── Auth ────────────────────────────────────────────────────────────────────

export interface AuthSessionType {
  accessToken: string;
  refreshToken: string;
  expiresAt: number;
  user: UserType;
}
