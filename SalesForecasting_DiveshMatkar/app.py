import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import IsolationForest

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():

    df = pd.read_csv("Outputs/clean_superstore.csv", encoding="latin1")

    df["Order Date"] = pd.to_datetime(df["Order Date"])

    return df


df = load_data()

st.sidebar.title("📊 Dashboard")

page = st.sidebar.radio(

    "Navigation",

    [

        "Sales Overview",

        "Forecast Explorer",

        "Anomaly Report",

        "Product Demand Segments",

        "Business Insights"

    ]

)

if page == "Sales Overview":

    st.title("📊 Sales Overview Dashboard")

    st.markdown(
        "Monitor overall sales performance using interactive visualizations."
    )
    
    st.sidebar.header("Filters")
    
    region = st.sidebar.multiselect(

        "Select Region",

        options=sorted(df["Region"].unique()),

        default=sorted(df["Region"].unique())

    )
    
    category = st.sidebar.multiselect(

        "Select Category",

        options=sorted(df["Category"].unique()),

        default=sorted(df["Category"].unique())

    )
    
    year = st.sidebar.multiselect(

        "Select Year",

        options=sorted(df["Order Date"].dt.year.unique()),

        default=sorted(df["Order Date"].dt.year.unique())

    )
    filtered_df = df[

        (df["Region"].isin(region))

        &

        (df["Category"].isin(category))

        &

        (df["Order Date"].dt.year.isin(year))

    ]

    st.subheader("📌 Key Performance Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Total Sales",

            f"${df['Sales'].sum():,.0f}"

        )


    with col2:

        st.metric(

            "Orders",

            df["Order ID"].nunique()

        )

    with col3:

        st.metric(

            "Customers",

            filtered_df["Customer ID"].nunique()

        )
    st.divider()
    
    sales_year = (

        filtered_df

        .groupby(filtered_df["Order Date"].dt.year)["Sales"]

        .sum()

        .reset_index()

    )

    sales_year.columns = ["Year", "Sales"]

    fig = px.bar(

        sales_year,

        x="Year",

        y="Sales",

        text_auto=".2s",

        color="Sales",

        title="Total Sales by Year"

    )

    st.plotly_chart(fig, width='stretch')

    monthly_sales = (

        filtered_df

        .groupby(

            pd.Grouper(

                key="Order Date",

                freq="ME"

            )

        )["Sales"]

        .sum()

        .reset_index()

    )

    fig = px.line(

        monthly_sales,

        x="Order Date",

        y="Sales",

        markers=True,

        title="Monthly Sales Trend"

    )

    st.plotly_chart(fig, width='stretch')

    left, right = st.columns(2)

    region_sales = (

        filtered_df

        .groupby("Region")["Sales"]

        .sum()

        .reset_index()

    )

    region_fig = px.pie(

        region_sales,

        names="Region",

        values="Sales",

        hole=0.45,

        title="Sales by Region"

    )

    with left:

        st.plotly_chart(

            region_fig,

            width='stretch'

        )
    category_sales = (

        filtered_df

        .groupby("Category")["Sales"]

        .sum()

        .reset_index()

    )

    category_fig = px.bar(

        category_sales,

        x="Category",

        y="Sales",

        color="Category",

        text_auto=".2s",

        title="Sales by Category"

    )

    with right:

        st.plotly_chart(

            category_fig,

            width='stretch'

        )
    top_products = (

        filtered_df

        .groupby("Sub-Category")["Sales"]

        .sum()

        .sort_values(ascending=False)

        .head(10)

        .reset_index()

    )

    fig = px.bar(

        top_products,

        x="Sales",

        y="Sub-Category",

        orientation="h",

        color="Sales",

        text_auto=".2s",

        title="Top 10 Sub-Categories by Sales"

    )

    st.plotly_chart(fig, width='stretch')

    
    st.subheader("📄 Filtered Dataset")

    st.dataframe(

        filtered_df,

        width='stretch'

    )
    
    csv = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Filtered Data",

        data=csv,

        file_name="filtered_sales.csv",

        mime="text/csv"

    )


elif page == "Forecast Explorer":

    st.title("📈 Forecast Explorer")

    st.markdown(
        "Explore sales forecasts using the **XGBoost** model."
    )
    forecast_type = st.selectbox(

        "Forecast By",

        [

            "Category",

            "Region"

        ]

    )
    if forecast_type == "Category":

        selected = st.selectbox(

            "Select Category",

            sorted(df["Category"].unique())

    )

    else:

        selected = st.selectbox(

            "Select Region",

            sorted(df["Region"].unique())

        )
    months = st.slider(

    "Forecast Horizon (Months)",

    min_value=1,

    max_value=3,

    value=3
    )
    
    forecast_table = pd.read_csv(
    "Outputs/Task4_Forecast_all.csv"
    )
    
    forecast_values = forecast_table[selected].iloc[:months]
    

    forecast_df = pd.DataFrame({

        "Month":[

            f"Month {i}"

            for i in range(1,months+1)

        ],

    "Forecast":forecast_values.values
    })

    fig = px.line(

        forecast_df,

        x="Month",

        y="Forecast",

        markers=True,

        title=f"{selected} Sales Forecast"
        )

    st.plotly_chart(

        fig,

        width='stretch'

    )
    st.subheader("Forecast Values")

    st.dataframe(

        forecast_df,

        width='stretch'

    )
    comparison = pd.read_csv(
        "Outputs/model_comparison.csv"
    )

    best = comparison[
        comparison["Model"]=="XGBoost"
    ]

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.metric(

            "Best Model",

            "XGBoost"

        )

    with c2:

        st.metric(

            "MAE",

            f"{best['MAE'].values[0]:.2f}"

        )

    with c3:

        st.metric(

            "RMSE",

            f"{best['RMSE'].values[0]:.2f}"

        )
    with c4:

        st.metric(

            "MAPE",

            "14.79%"

        )

    st.info(

    """
    ### Business Insight

    The forecast displayed above is generated using the **XGBoost** model,
    which achieved the lowest forecasting error among all evaluated models.

    This forecast can help managers estimate future demand and make informed
    inventory and procurement decisions.

    """
    )

elif page == "Anomaly Report":

    st.title("🚨 Anomaly Report")

    st.markdown(
        "Identify unusual sales patterns detected using the Isolation Forest algorithm."
    )

    st.divider()
    
    weekly_sales = (
        df.groupby(pd.Grouper(key="Order Date", freq="W"))["Sales"]
        .sum()
        .to_frame()
    )
    
    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    weekly_sales["Prediction"] = model.fit_predict(
        weekly_sales[["Sales"]]
    )

    weekly_sales["Anomaly"] = weekly_sales["Prediction"].map({
        1: "Normal",
        -1: "Anomaly"
    })
    
    anomaly_df = weekly_sales[
        weekly_sales["Anomaly"] == "Anomaly"
    ].copy()

    anomaly_df.reset_index(inplace=True)
    
    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Total Weeks",
            len(weekly_sales)
        )

    with c2:
        st.metric(
            "Detected Anomalies",
            len(anomaly_df)
        )
        
        import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=weekly_sales.index,
            y=weekly_sales["Sales"],
            mode="lines",
            name="Weekly Sales"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=anomaly_df["Order Date"],
            y=anomaly_df["Sales"],
            mode="markers",
            name="Anomaly",
            marker=dict(
                color="red",
                size=10,
                symbol="x"
            )
        )
    )

    fig.update_layout(
        title="Weekly Sales with Detected Anomalies",
        xaxis_title="Week",
        yaxis_title="Sales",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        width='stretch'
    )
    st.subheader("📋 Detected Anomalies")

    anomaly_table = anomaly_df[
        [
            "Order Date",
            "Sales"
        ]
    ]

    anomaly_table.columns = [
        "Date",
        "Sales"
    ]

    st.dataframe(
        anomaly_table,
        width='stretch'
    )
    
    csv = anomaly_table.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Anomaly Report",
        csv,
        file_name="anomaly_report.csv",
        mime="text/csv"
    )
    
    st.info("""
        ### Business Insight

        The highlighted weeks represent unusual sales behavior detected by the Isolation Forest algorithm.

        Possible reasons include:

        - Festive season demand
        - Promotional campaigns
        - Flash sales
        - Supply chain disruptions
        - Inventory shortages

        These periods should be investigated to improve demand planning and inventory management.
        """)
    
elif page == "Product Demand Segments":

    st.title("📦 Product Demand Segments")

    st.markdown(
        """
        Explore the product demand clusters generated using the
        **K-Means Clustering** algorithm.
        """
    )

    st.divider()
    
    segment_df = pd.read_csv(
        "Outputs/Product_Segmentation.csv")
    
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Sub-Categories",
            segment_df.shape[0]
        )

    with col2:

        st.metric(
            "Clusters",
            segment_df["Demand Segment"].nunique()
        )

    with col3:

        st.metric(
            "Algorithm",
            "K-Means"
        )
        
    import plotly.express as px

    
    fig = px.treemap(
    segment_df,
    path=["Demand Segment", "Sub-Category"],
    values="Total Sales",
    color="Demand Segment",
    title="Demand Segments by Sales")

    st.plotly_chart(fig, width='stretch')
    
    fig = px.scatter(
    segment_df,
    x="Number of Orders",
    y="Average Sales",
    size="Total Sales",
    color="Demand Segment",
    hover_name="Sub-Category",
    title="Demand Segmentation")

    st.plotly_chart(fig, width='stretch')
    
    st.subheader("📦 Demand Segment Distribution")
    
    segments = sorted(
    segment_df["Demand Segment"].unique())

    selected_segment = st.selectbox(

        "Select Demand Segment",

        segments

    )
    
    filtered_segment = segment_df[

    segment_df["Demand Segment"] == selected_segment]
    
    st.subheader("📋 Sub-Categories")

    st.dataframe(

        filtered_segment[
            [
                "Sub-Category",
                "Total Sales",
                "Average Sales",
                "Number of Orders",
                "Demand Segment"
            ]
        ],

        width='stretch'

    )
    
    csv = filtered_segment.to_csv(

    index=False).encode("utf-8")

    st.download_button(

        "📥 Download Cluster Report",

        csv,

        "Product_Segmentation.csv",

        "text/csv"

    )
    
    st.subheader("📦 Recommended Stocking Strategy")

    if selected_segment == "High Demand":

        st.success(
            """
    **Recommendation**

    • Maintain high inventory levels.

    • Restock frequently to prevent stock shortages.

    • Prioritize these products during peak demand periods.
    """
        )

    elif selected_segment == "Moderate Demand":

        st.info(
            """
    **Recommendation**

    • Maintain balanced inventory.

    • Use regular replenishment based on demand.
    """
        )

    elif selected_segment == "Low Demand":

        st.warning(
            """
    **Recommendation**

    • Keep limited inventory.

    • Replenish only when necessary to reduce storage costs.
    """
        )

    else:

        st.info(
            """
    **Recommendation**

    • Maintain moderate stock levels.

    • Monitor demand carefully because these products have higher value.
    """
        )
        
    st.info(
        """
        ### Business Insight

        K-Means clustering groups products with similar sales patterns.

        This segmentation helps the business:

        - Optimize inventory allocation
        - Reduce excess stock
        - Improve procurement planning
        - Prioritize high-demand products
        - Lower warehouse holding costs
        """
        )

elif page == "Business Insights":

    st.title("💡 Business Insights")

    st.markdown(
        """
        This dashboard summarizes the key findings and business recommendations
        generated from the Sales Forecasting & Demand Intelligence System.
        """
    )

    st.divider()

    # ============================
    # Project Summary
    # ============================

    st.subheader("📊 Project Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Best Model", "XGBoost")

    with col2:
        st.metric("MAE", "15,169")

    with col3:
        st.metric("RMSE", "19,041")

    with col4:
        st.metric("MAPE", "14.79 %")

    st.divider()

    # ============================
    # Key Insights
    # ============================

    st.subheader("📈 Key Insights")

    st.success("""
**Sales Analysis**

• Sales show an overall increasing trend with seasonal fluctuations.

• Technology products contribute significantly to total revenue.

• Western and Eastern regions generate the highest sales.

• Several unusual sales spikes were detected during promotional periods.
""")

    st.divider()

    # ============================
    # Forecast Insights
    # ============================

    st.subheader("🔮 Forecast Insights")

    st.info("""
• XGBoost achieved the lowest forecasting error among all models.

• Future sales are expected to remain stable with gradual growth.

• Forecasting can help optimize inventory planning and purchasing decisions.
""")

    st.divider()

    # ============================
    # Demand Segmentation
    # ============================

    st.subheader("📦 Product Demand Insights")

    st.warning("""
• High-demand products should be prioritized for inventory allocation.

• Moderate-demand products require regular replenishment.

• Low-demand products should be stocked conservatively.

• Premium products should be monitored carefully due to their higher value.
""")

    st.divider()

    # ============================
    # Business Recommendations
    # ============================

    st.subheader("💼 Business Recommendations")

    recommendations = [
        "Increase inventory for high-demand products.",
        "Use XGBoost forecasts for monthly inventory planning.",
        "Monitor anomaly periods before making inventory decisions.",
        "Reduce excess stock for low-demand products.",
        "Focus marketing campaigns on high-performing categories.",
        "Review premium products periodically to maximize profitability."
    ]

    for i, rec in enumerate(recommendations, start=1):
        st.write(f"**{i}.** {rec}")

    st.divider()

    # ============================
    # Executive Summary
    # ============================

    st.subheader("📋 Executive Summary")

    st.info("""
        The Sales Forecasting & Demand Intelligence System combines machine learning,
        time series forecasting, anomaly detection, and product segmentation to
        support better business decision-making.

        The XGBoost model delivered the highest forecasting accuracy. Demand
        segmentation identified products with different sales behaviors, while
        anomaly detection highlighted unusual sales events that require further
        investigation.

        These insights enable businesses to improve inventory management, optimize
        procurement, reduce storage costs, and make data-driven strategic decisions.
        """)

    st.divider()

    # ============================
    # Download Summary
    # ============================

    report = """
        Sales Forecasting & Demand Intelligence System

        Best Forecasting Model : XGBoost

        Key Findings
        -------------
        • Overall sales show an increasing trend.
        • Seasonal demand patterns were identified.
        • XGBoost achieved the best forecasting performance.
        • Four product demand segments were created.
        • Sales anomalies were successfully detected.

        Business Recommendations
        ------------------------
        • Increase stock for high-demand products.
        • Reduce inventory for low-demand products.
        • Use forecasting for inventory planning.
        • Monitor anomalies regularly.
        """

    st.download_button(
        "📥 Download Business Summary",
        report,
        file_name="Business_Insights.txt",
        mime="text/plain"
    )