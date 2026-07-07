"""
=========================================================
Project Configuration
Sales Forecasting & Demand Intelligence System
=========================================================
"""

from pathlib import Path

# =========================================================
# Project Root
# =========================================================

ROOT_DIR = Path(__file__).resolve().parent

# =========================================================
# Data
# =========================================================

DATA_DIR = ROOT_DIR / "data"

TRAIN_DATA = DATA_DIR / "train.csv"

VGSALES_DATA = DATA_DIR / "vgsales.csv"

# =========================================================
# Notebook
# =========================================================

NOTEBOOK_DIR = ROOT_DIR / "Notebooks"

# =========================================================
# Output Folders
# =========================================================

CHART_DIR = ROOT_DIR / "Charts"

MODEL_DIR = ROOT_DIR / "Models"

OUTPUT_DIR = ROOT_DIR / "Outputs"

REPORT_DIR = ROOT_DIR / "Reports"

FORECAST_DIR = ROOT_DIR / "Forecasts"

LOG_DIR = ROOT_DIR / "logs"

ASSET_DIR = ROOT_DIR / "Assets"

# =========================================================
# Automatically Create Folders
# =========================================================

directories = [
    CHART_DIR,
    MODEL_DIR,
    OUTPUT_DIR,
    REPORT_DIR,
    FORECAST_DIR,
    LOG_DIR,
    ASSET_DIR
]

for folder in directories:
    folder.mkdir(parents=True, exist_ok=True)