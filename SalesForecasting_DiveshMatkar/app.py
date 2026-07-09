import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

from config import OUTPUT_DIR, CHART_DIR

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Forecasting & Demand Intelligence Dashboard")

st.markdown("---")

comparison = pd.read_csv(
    OUTPUT_DIR/"model_comparison.csv"
)

best_model = comparison.loc[
    comparison["RMSE"].idxmin(),
    "Model"
]

forecast = pd.read_csv(
    OUTPUT_DIR/"Task4_Forecast.csv"
)

total_forecast = forecast.iloc[:,1:].sum().sum()

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Best Model",
        best_model
    )

with col2:
    st.metric(
        "Forecast Months",
        "3"
    )

with col3:
    st.metric(
        "Forecast Sales",
        f"{total_forecast:,.0f}"
    )
    
st.header("Monthly Sales Trend")

image = Image.open(
    CHART_DIR/"07_monthly_sales.png"
)

st.image(image,use_container_width=True)

st.header("XGBoost Forecast")

image = Image.open(
    CHART_DIR/"25_xgboost_forecast.png"
)

st.image(image,use_container_width=True)

st.header("Category & Region Forecast")

image = Image.open(
    CHART_DIR/"28_Task4_Forecast.png"
)

st.image(image,use_container_width=True)

# st.header("Anomaly Detection")

# image = Image.open(
#     CHART_DIR/"50_anomaly_comparison.png"
# )

st.image(image,use_container_width=True)

st.header("Product Demand Segmentation")

image = Image.open(
    CHART_DIR/"52_clusters.png"
)

st.image(image,use_container_width=True)

st.header("Forecast Results")

forecast = pd.read_csv(
    OUTPUT_DIR/"Task4_Forecast.csv"
)

st.dataframe(
    forecast,
    use_container_width=True
)

csv = forecast.to_csv(index=False).encode("utf-8")

st.download_button(

    "📥 Download Forecast",

    csv,

    "Forecast.csv",

    "text/csv"

)

st.header("Business Summary")

st.success("""

✔ XGBoost achieved the best forecasting performance.

✔ Technology and high-growth regions should receive higher inventory allocation.

✔ Isolation Forest and Z-Score successfully detected unusual sales periods.

✔ Product segmentation supports better inventory planning.

""")