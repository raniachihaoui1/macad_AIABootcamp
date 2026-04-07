"""
EDA Streamlit App — Template

This is a skeleton for your Streamlit app. Fill in the TODOs with code
from your notebooks (Exercises 01-04).

Run locally:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# ──────────────────────────────────────────────
# 1. Page config (must be the first st command)
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="My City EDA",  # TODO: change to your city
    page_icon="🏙️",
    layout="wide",
)

# ──────────────────────────────────────────────
# 2. Data loading (cached)
# ──────────────────────────────────────────────
@st.cache_data
def load_data():
    """Load your cleaned data.

    TODO: Update the file path to your city's clean CSV.
    Add any normalization from Exercise 03 here.
    """
    # TODO: change the path to your city's CSV
    df = pd.read_csv("data/clean_your_city.csv")

    # TODO: add cuisine normalization, hours classification, etc.
    # (copy from Exercise 03)

    return df


df = load_data()

# ──────────────────────────────────────────────
# 3. Sidebar — Filters
# ──────────────────────────────────────────────
st.sidebar.header("Filters")

# TODO: Add a multiselect for amenity types
# selected_amenities = st.sidebar.multiselect(
#     "Amenity types",
#     options=sorted(df["amenity"].dropna().unique()),
#     default=sorted(df["amenity"].dropna().unique())[:10],
# )

# TODO: Filter the dataframe based on selection
# df_filtered = df[df["amenity"].isin(selected_amenities)]
df_filtered = df  # Remove this line once you add the filter above

# ──────────────────────────────────────────────
# 4. Main area — Title
# ──────────────────────────────────────────────
st.title("🏙️ My City Amenities")  # TODO: change to your city name
st.markdown("Exploratory Data Analysis of OpenStreetMap amenity data.")

# ──────────────────────────────────────────────
# 5. KPI metrics
# ──────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

# TODO: Fill in the metrics
col1.metric("Total Amenities", len(df_filtered))
col2.metric("Amenity Types", df_filtered["amenity"].nunique())
# col3.metric("Have Names", f"{df_filtered['primary_name'].notna().mean()*100:.0f}%")

# ──────────────────────────────────────────────
# 6. Map
# ──────────────────────────────────────────────
st.subheader("Map")

# TODO: Create a plotly scatter_mapbox and display it
# fig = px.scatter_mapbox(
#     df_filtered,
#     lat="lat",
#     lon="lon",
#     color="amenity",
#     hover_name="primary_name",
#     mapbox_style="carto-positron",
#     zoom=11,
#     height=500,
# )
# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# st.plotly_chart(fig, use_container_width=True)

st.info("TODO: Add your map here")

# ──────────────────────────────────────────────
# 7. Charts
# ──────────────────────────────────────────────
st.subheader("Charts")

# TODO: Add at least one chart (copy from Exercise 04)
# Example: bar chart of top amenity types
# amenity_counts = df_filtered["amenity"].value_counts().head(15)
# fig_bar = px.bar(x=amenity_counts.values, y=amenity_counts.index, orientation="h")
# st.plotly_chart(fig_bar, use_container_width=True)

st.info("TODO: Add your charts here")

# ──────────────────────────────────────────────
# 8. Footer
# ──────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "Data: [OpenStreetMap](https://www.openstreetmap.org/copyright) · "
    "Built with [Streamlit](https://streamlit.io/)"
)
