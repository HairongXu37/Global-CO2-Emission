"""
ARIMA model training and evaluation.
"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(series: pd.Series, order=(2, 1, 2)):
    """
    Fit an ARIMA model to the series.

    Parameters:
        series (pd.Series): Stationary time series.
        order (tuple): ARIMA(p,d,q)

    Returns:
        ARIMAResultsWrapper: Fitted model.
    """
    model = ARIMA(series, order=order)
    return model.fit()

def plot_arima_fit(fitted_model, original_series: pd.Series):
    """
    Plot ARIMA predictions against original series.

    Parameters:
        fitted_model: Fitted ARIMA model.
        original_series (pd.Series): Stationary series.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(original_series, label="Original")
    plt.plot(fitted_model.fittedvalues, color='black', linestyle='--', label="ARIMA Fitted")
    plt.title("ARIMA Forecast vs Original")
    plt.legend()
    plt.grid(True)
    plt.show()
