"""
Data loading and preparation for CO₂ emissions time series.
"""

import pandas as pd

def load_emission_data(path: str) -> pd.DataFrame:
    """
    Load and return emissions data filtered from year 1950.

    Parameters:
        path (str): Path to emissions CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = pd.read_csv(path)
    df = df[df['Year'] >= 1950]
    return df

def filter_global_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter for global (WLD) data only.

    Parameters:
        df (pd.DataFrame): Emissions DataFrame.

    Returns:
        pd.DataFrame: Global rows only.
    """
    return df[df['ISO 3166-1 alpha-3'] == 'WLD'].copy()
