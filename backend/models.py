from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="The title of the todo item")
    description: Optional[str] = Field(None, max_length=1000, description="Detailed description of the todo item")
    completed: bool = Field(False, description="Completion status of the todo item")


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="The title of the todo item")
    description: Optional[str] = Field(None, max_length=1000, description="Detailed description of the todo item")
    completed: Optional[bool] = Field(None, description="Completion status of the todo item")


class Todo(TodoBase):
    id: int = Field(..., description="Unique identifier for the todo item")
    created_at: datetime = Field(..., description="Timestamp when the todo item was created")
    updated_at: Optional[datetime] = Field(None, description="Timestamp when the todo item was last updated")

    class Config:
        from_attributes = True


# --- Financial Portfolio Simulator & Monte Carlo Risk Engine Models ---

class AssetWeights(BaseModel):
    equities: float = Field(..., ge=0.0, le=100.0, description="Allocation weight for Equities (%)")
    tech: float = Field(..., ge=0.0, le=100.0, description="Allocation weight for Tech (%)")
    fixed_income: float = Field(..., ge=0.0, le=100.0, description="Allocation weight for Fixed Income (%)")
    crypto: float = Field(..., ge=0.0, le=100.0, description="Allocation weight for Crypto (%)")
    gold: float = Field(..., ge=0.0, le=100.0, description="Allocation weight for Gold (%)")


class BacktestConfig(BaseModel):
    weights: AssetWeights = Field(..., description="Asset allocation weights")
    initial_capital: float = Field(100000.0, gt=0.0, description="Initial portfolio capital")
    years: int = Field(5, ge=1, le=10, description="Number of historical years to simulate")
    volatility_multiplier: float = Field(1.0, gt=0.0, description="Multiplier for asset volatility")
    drift_multiplier: float = Field(1.0, description="Multiplier for asset drift/return")
    simulate_crash: bool = Field(False, description="Whether to inject a market crash event")
    crash_day_offset: int = Field(500, ge=0, description="Day offset from start when crash occurs")
    crash_severity: float = Field(0.25, ge=0.0, le=0.9, description="Severity of the crash (e.g. 0.25 = 25% drop)")


class RiskMetrics(BaseModel):
    sharpe_ratio: float = Field(..., description="Annualized Sharpe Ratio")
    sortino_ratio: float = Field(..., description="Annualized Sortino Ratio")
    max_drawdown: float = Field(..., description="Maximum Drawdown (percentage)")
    value_at_risk_95: float = Field(..., description="Historical Value at Risk at 95% confidence (percentage or amount)")
    cvar_95: Optional[float] = Field(None, description="Conditional Value at Risk (Expected Shortfall) at 95%")
    annualized_return: float = Field(..., description="Annualized Return")
    annualized_volatility: float = Field(..., description="Annualized Volatility")
    total_return: float = Field(..., description="Total cumulative return percentage")


class TimeSeriesPoint(BaseModel):
    date: str = Field(..., description="Date string YYYY-MM-DD")
    portfolio_value: float = Field(..., description="Portfolio value")
    benchmark_value: float = Field(..., description="S&P 500 benchmark value")
    drawdown: float = Field(..., description="Current drawdown percentage")


class BacktestResponse(BaseModel):
    config: BacktestConfig = Field(..., description="Configuration used for backtest")
    metrics: RiskMetrics = Field(..., description="Calculated risk metrics")
    time_series: List[TimeSeriesPoint] = Field(..., description="Daily time-series data for portfolio and benchmark")
    asset_returns: Dict[str, float] = Field(..., description="Cumulative return per asset class")


class MonteCarloConfig(BaseModel):
    weights: AssetWeights = Field(..., description="Asset allocation weights")
    initial_capital: float = Field(100000.0, gt=0.0, description="Initial portfolio capital")
    horizon_days: int = Field(365, ge=30, le=1095, description="Forward-looking simulation horizon in days")
    num_simulations: int = Field(100, ge=10, le=1000, description="Number of Monte Carlo path trajectories")
    confidence_level: float = Field(0.95, gt=0.0, lt=1.0, description="Confidence level for VaR/Percentiles")


class MonteCarloPercentilePath(BaseModel):
    day: int = Field(..., description="Day index (0 to horizon_days)")
    p5: float = Field(..., description="5th percentile portfolio value")
    p25: float = Field(..., description="25th percentile portfolio value")
    p50: float = Field(..., description="Median (50th percentile) portfolio value")
    p75: float = Field(..., description="75th percentile portfolio value")
    p95: float = Field(..., description="95th percentile portfolio value")
    mean: float = Field(..., description="Mean simulated portfolio value")


class MonteCarloResponse(BaseModel):
    config: MonteCarloConfig = Field(..., description="Configuration used for Monte Carlo simulation")
    percentile_paths: List[MonteCarloPercentilePath] = Field(..., description="Aggregated percentile paths for fan chart")
    sample_paths: List[List[float]] = Field(..., description="Subset of individual simulation paths for rendering")
    final_value_distribution: Dict[str, float] = Field(..., description="Summary statistics of final values (mean, median, p5, p95, var_95)")

