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

/**
 * Financial Portfolio Simulator and Risk Engine Types
 */
export interface AssetAllocation {
  equities: number;
  tech: number;
  fixedIncome: number;
  crypto: number;
  gold: number;
}

export interface RiskMetrics {
  sharpeRatio: number;
  sortinoRatio: number;
  maxDrawdown: number;
  var95: number;
  annualizedReturn: number;
  annualizedVolatility: number;
}

export interface SimulationParams {
  initialCapital: number;
  years: number;
  volatility: number;
  drift: number;
  crashMagnitude: number;
  crashDay: number;
}

export interface DataPoint {
  date: string;
  portfolioValue: number;
  benchmarkValue: number;
}

export interface MonteCarloPath {
  day: number;
  values: number[];
}

export interface MonteCarloResult {
  paths: number[][]; // [pathIndex][dayIndex]
  percentiles: {
    p10: number[];
    p25: number[];
    median: number[];
    p75: number[];
    p90: number[];
  };
  days: number[];
}

