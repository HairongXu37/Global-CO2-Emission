"""
Time series transformation utilities.
"""

import pandas as pd
from statsmodels.tsa.stattools import adfuller

def build_stationary_series(df: pd.DataFrame) -> pd.Series:
    """
    Transform total emissions into a rolling stationary series.

    Parameters:
        df (pd.DataFrame): DataFrame with 'Total' column and 'Year'.

    Returns:
        pd.Series: Stationary series.
    """
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-01-01')
    df.set_index('Date', inplace=True)
    df = df[['Total']]
    df['roll12'] = df['Total'].rolling(window=12).mean()
    df.dropna(inplace=True)
    df.index.freq = 'YS'  # ✅ Explicitly set frequency
    return df['roll12']    

def adf_test(series: pd.Series, max_lag: int = 12):
    """
    Perform ADF test for multiple lags to test stationarity.

    Parameters:
        series (pd.Series): Time series.
        max_lag (int): Max lags to test.

    Returns:
        dict: ADF stats and p-values.
    """
    results = {}
    for lag in range(1, max_lag + 1):
        adf, pval, *_ = adfuller(series, regression='ct', maxlag=lag)
        results[lag] = {'adf_stat': adf, 'p_value': pval}
    return results
