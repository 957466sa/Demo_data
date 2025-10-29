import streamlit as st
import pandas as pd

st.title("📊 Sales Dashboard")

# Load CSV from GitHub (raw link)
url = "https://raw.githubusercontent.com/957466sa/DBT_DEMO/main/data/sales_data.csv"
data = pd.read_csv(url)

st.subheader("Raw Data")
st.dataframe(data)

# Simple chart
st.subheader("Total Sales by Region")
chart_data = data.groupby("region")["sales"].sum().reset_index()
st.bar_chart(chart_data, x="region", y="sales")

st.success("✅ Data loaded successfully from GitHub!")
