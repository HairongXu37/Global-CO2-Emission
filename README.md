
---

## 📊 Part 1: Exploratory Data Analysis (EDA)

Implemented in `emissions_eda.ipynb` using clean pipeline logic in `src/pipeline.py` and visualizations in `visualizations/plots.py`.

### Highlights:

- Cleaned and imputed missing values by country-sector mean  
- Dropped irrelevant global/international transport data  
- Visualized:
  - Top emitters over time
  - Sector-wise trends for USA, India, Afghanistan
  - Correlation heatmaps
  - Choropleth maps (Coal, Gas, Cement, etc.)
  - Per capita emissions  
- Explained key trends (e.g., rise of coal in USA, dip in 2020 from COVID-19)

✅ The EDA serves as both an **analytical deep-dive** and **pipeline-ready visualization tool**.

---

## 🔮 Part 2: Time Series Forecasting

Implemented as a clean forecasting pipeline with modular Python components and a controller notebook.

### Features:

- Filters **only global data** (ISO code `'WLD'`)  
- Removes data before 1950  
- Makes time series **stationary** using 12-year rolling average  
- Runs **ADF stationarity test**  
- Trains an **ARIMA(2,1,2)** model  
- Visualizes original series vs. model predictions  

### Modules (inside `src/`):

- `data_loader.py`: Load and filter data  
- `transform.py`: Stationarize series  
- `model.py`: Train ARIMA and plot results  

---

## 📈 Forecasting Output

The forecasting notebook plots:

- Global CO₂ emissions (stationary)  
- ARIMA model fitted predictions  

✅ Model setup supports `.forecast(steps=5)` for future years (extendable)

---

## ▶️ How to Run

1. Clone this repo  
2. Place the dataset in `data/GCB2022v27_MtCO2_flat.csv`  
3. Run:
   - `emissions_eda.ipynb` for EDA  
   - `time_series_forecasting.ipynb` for forecasting  

---
