/**
 * TypeScript interfaces and types for Todo items matching the FastAPI backend models.
 */

export interface Todo {
  id: number;
  title: string;
  description?: string | null;
  completed: boolean;
  created_at: string;
  updated_at?: string | null;
}

export interface TodoCreate {
  title: string;
  description?: string | null;
  completed?: boolean;
}

export interface TodoUpdate {
  title?: string;
  description?: string | null;
  completed?: boolean;
}

export interface TodoFilter {
  skip?: number;
  limit?: number;
  completed?: boolean;
}
