# Demand Shock & Forecast Resilience Analytics Platform (DSFR)

An end-to-end analytics project that simulates retail demand, builds a SQLite analytics warehouse, trains an interpretable forecasting model, detects demand shocks, and quantifies revenue impact under scenario stress tests. Output tables and CSV exports are Power BI-ready.

## What this project demonstrates
- Data modeling (star-ish schema) in SQLite
- Time-series feature engineering (lags + rolling stats)
- Forecast evaluation (MAPE, bias) + drift monitoring
- Shock detection via rolling residual z-score
- Financial impact simulation (lost sales vs overstock cost)
- BI handoff (CSV exports + DAX/relationship guidance)

## Repo structure
- `sql/schema.sql` – warehouse schema
- `src/dsfr/pipelines/` – generation, features, modeling, shocks, scenarios
- `scripts/` – CLI entrypoints (one command or step-by-step)
- `outputs/` – created when you run pipelines (DB + CSVs)
- `docs/powerbi_setup.md` – relationships + measures + page layout

## Quickstart (recommended)
### 1) Create venv + install
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run the full pipeline
```bash
# Windows PowerShell: $env:PYTHONPATH="src"
export PYTHONPATH=src
bash scripts/run_all.sh outputs/dsfr.sqlite
```

Outputs:
- SQLite DB: `outputs/dsfr.sqlite`
- Power BI exports: `outputs/powerbi/*.csv`

## Step-by-step (optional)
```bash
export PYTHONPATH=src
python scripts/create_db.py outputs/dsfr.sqlite
python scripts/generate_data.py outputs/dsfr.sqlite --days 1095 --skus 50 --stores 8 --seed 42
python scripts/train_forecast.py outputs/dsfr.sqlite --horizon 30
python scripts/detect_shocks.py outputs/dsfr.sqlite --z 3.0
python scripts/simulate_scenarios.py outputs/dsfr.sqlite --shocks "-0.40,-0.25,-0.10,0.10,0.25,0.40"
python scripts/export_for_powerbi.py outputs/dsfr.sqlite outputs/powerbi
```

## Power BI guidance
See `docs/powerbi_setup.md` for:
- model relationships
- DAX measures (forecast, shocks, scenario impact)
- recommended dashboard pages

## Notes
- The data generator injects **sudden spikes/drops** to create realistic demand shocks.
- The baseline forecaster is a Ridge regression on lag features (fast, interpretable).
- You can swap in ARIMA/Prophet later without changing the warehouse contract.
