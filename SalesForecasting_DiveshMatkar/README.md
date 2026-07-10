# 📈 Sales Forecasting & Demand Intelligence System

A Machine Learning and Time Series Forecasting project developed during the **XYlofy AI Internship (Week 3–4)**. The system forecasts future sales, detects unusual sales patterns, segments products based on demand, and provides an interactive Streamlit dashboard for business decision-making.

---

## 📌 Project Objective

The objective of this project is to build an intelligent sales forecasting system that helps businesses:

- Forecast future sales accurately.
- Detect unusual sales behavior (anomalies).
- Segment products based on demand.
- Support inventory planning.
- Provide business insights through an interactive dashboard.

---

## 📂 Datasets

### Primary Dataset
- Superstore Sales Dataset (`train.csv`)

---

## 🚀 Features

- Advanced Exploratory Data Analysis (EDA)
- Time Series Analysis
- Stationarity Testing (ADF Test)
- Sales Forecasting using:
  - SARIMA
  - Prophet
  - XGBoost
- Model Comparison
- Category & Region-wise Forecasting
- Anomaly Detection
  - Isolation Forest
  - Z-Score Method
- Product Demand Segmentation using K-Means Clustering
- Interactive Streamlit Dashboard
- Business Insights & Recommendations

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- XGBoost
- Prophet
- Statsmodels
- Streamlit
- Joblib

---

## 📁 Project Structure

```text
SalesForecasting/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── train.csv
│   └── vgsales.csv
│
├── Models/
│
├── Charts/
│
├── Outputs/
│
├── utils/
│   ├── helper.py
│   └── logger.py
│
└── notebooks/
```

---

## 📊 Workflow

### 1. Data Preparation
- Load datasets
- Data cleaning
- Feature engineering
- Date conversion

### 2. Exploratory Data Analysis
- Sales trend
- Category analysis
- Region analysis
- Monthly sales
- Seasonal analysis

### 3. Time Series Analysis
- Stationarity Test (ADF)
- Differencing (if required)

### 4. Forecasting Models
- SARIMA
- Prophet
- XGBoost

### 5. Model Evaluation

Models are evaluated using:

- MAE
- RMSE
- MAPE

The model with the lowest forecasting error is selected.

---

## 🏆 Best Model

| Model | MAE | RMSE | MAPE |
|--------|---------:|---------:|---------:|
| SARIMA | 20581.00 | 22191.27 | 21.94% |
| Prophet | 20250.79 | 22318.41 | 21.86% |
| **XGBoost** | **15169.05** | **19040.85** | **14.79%** |

**XGBoost** achieved the best forecasting performance and was selected as the final production model.

---

## 🚨 Anomaly Detection

Two anomaly detection techniques were applied:

- Isolation Forest
- Z-Score

These methods help identify unusual sales spikes or drops that may result from promotions, seasonal demand, or unexpected events.

---

## 📦 Product Demand Segmentation

Products were grouped using the **K-Means Clustering** algorithm into different demand segments:

- High Demand
- Moderate Demand
- Low Demand
- Premium Products

This segmentation supports inventory optimization and demand-driven business decisions.

---

## 📊 Streamlit Dashboard

The project includes an interactive dashboard with:

### Page 1 – Sales Overview
- KPI Cards
- Sales by Year
- Monthly Sales Trend
- Sales by Region
- Sales by Category

### Page 2 – Forecast Explorer
- Category/Region Selection
- Forecast Horizon
- Dynamic XGBoost Forecast
- Model Performance Metrics

### Page 3 – Anomaly Report
- Anomaly Detection Chart
- Anomaly Report Table

### Page 4 – Product Demand Segments
- Interactive Cluster Visualization
- Demand Segment Table
- Stocking Recommendations

### Page 5 – Business Insights
- Key Findings
- Business Recommendations
- Executive Summary

---

## 📈 Business Insights

Key insights generated from the project include:

- Sales exhibit an overall upward trend with seasonal fluctuations.
- XGBoost provides the most accurate sales forecasts.
- Isolation Forest successfully identifies unusual sales periods.
- Product segmentation enables better inventory planning and stock management.

---

## ▶️ How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Create Environment

```bash
conda create -n sales_forecasting python=3.11
```

```bash
conda activate sales_forecasting
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run app.py
```

---

## 📸 Dashboard Preview

The dashboard provides interactive visualizations for:

- Sales Analysis
- Forecasting
- Anomaly Detection
- Demand Segmentation
- Business Insights

---

## 🎯 Future Improvements

- Real-time sales forecasting
- Cloud deployment
- Automated data pipeline
- Email alert system for anomalies
- Live dashboard updates
- Advanced demand prediction using LSTM

---

## 👨‍💻 Author

**Divesh Matkar**

BCA Student | Aspiring AI Engineer

### Skills

- Machine Learning
- Data Science
- Time Series Forecasting
- Large Language Models (LLMs)
- FastAPI
- Streamlit
- LangChain

---

## 📄 License

This project was developed for educational and internship purposes under the **XYlofy AI Internship Program**.