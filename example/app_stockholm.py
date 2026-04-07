"""
Stockholm EDA — Reference Streamlit App

This is the teacher's reference implementation showing how notebook code
translates into a production Streamlit app. Students use this as a guide
for building their own app.py for their assigned city.

Run locally:
    cd example/
    streamlit run app_stockholm.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import osmnx as ox
import os

# ──────────────────────────────────────────────
# Page config (must be first Streamlit command)
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Stockholm Amenities — EDA",
    page_icon="🏙️",
    layout="wide",
)

# ──────────────────────────────────────────────
# Data loading (cached so it only runs once)
# ──────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "clean_stockholm.csv")

@st.cache_data
def load_data():
    """Load cleaned Stockholm data. Falls back to fetching with OSMnx."""

    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
    else:
        # Fetch with OSMnx if no local file (curated subset to limit API load)
        amenity_types = [
            "restaurant", "cafe", "fast_food", "bar", "pub",
            "pharmacy", "hospital", "clinic", "dentist",
            "school", "university", "library", "kindergarten",
            "bank", "atm", "post_office",
        ]
        gdf = ox.features_from_place("Stockholm, Sweden", tags={"amenity": amenity_types})
        gdf = gdf.reset_index()
        gdf["lat"] = gdf.geometry.centroid.y
        gdf["lon"] = gdf.geometry.centroid.x
        df = pd.DataFrame(gdf.drop(columns=["geometry"]))
        if "osmid" in df.columns:
            df = df.rename(columns={"osmid": "id"})

        # Basic cleaning
        df = df.dropna(subset=["lat", "lon"])
        df = df.drop_duplicates(subset=["lat", "lon"], keep="first")

        # Primary name
        df["primary_name"] = df.get("name", pd.Series(dtype=str))

    return df

df = load_data()

# ──────────────────────────────────────────────
# Normalize cuisine (same logic as notebook)
# ──────────────────────────────────────────────
def normalize_cuisine(value):
    if pd.isna(value):
        return "Unknown"
    parts = str(value).replace(",", ";").split(";")
    return parts[0].strip().lower().replace("_", " ").title()

if "cuisine" in df.columns:
    df["cuisine_clean"] = df["cuisine"].apply(normalize_cuisine)
else:
    df["cuisine_clean"] = "Unknown"

# ──────────────────────────────────────────────
# Sidebar — Filters
# ──────────────────────────────────────────────
st.sidebar.header("Filters")

# Amenity type filter
all_amenities = sorted(df["amenity"].dropna().unique())
selected_amenities = st.sidebar.multiselect(
    "Amenity types",
    options=all_amenities,
    default=all_amenities[:10],
    help="Select which amenity types to show on the map",
)

# Map style
map_style = st.sidebar.selectbox(
    "Map style",
    options=["carto-positron", "carto-darkmatter", "open-street-map"],
    index=0,
)

# Filter data
if selected_amenities:
    df_filtered = df[df["amenity"].isin(selected_amenities)]
else:
    df_filtered = df

# ──────────────────────────────────────────────
# Main area — Title
# ──────────────────────────────────────────────
st.title("🏙️ Stockholm Amenities Explorer")
st.markdown("Interactive exploration of OpenStreetMap amenity data for Stockholm.")

# ──────────────────────────────────────────────
# KPI row
# ──────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Amenities", f"{len(df_filtered):,}")
col2.metric("Amenity Types", df_filtered["amenity"].nunique())
col3.metric(
    "Have Names",
    f"{df_filtered['primary_name'].notna().mean() * 100:.0f}%"
    if "primary_name" in df_filtered.columns
    else "N/A",
)
col4.metric(
    "Have Cuisine",
    f"{(df_filtered['cuisine_clean'] != 'Unknown').mean() * 100:.0f}%"
    if "cuisine_clean" in df_filtered.columns
    else "N/A",
)

# ──────────────────────────────────────────────
# Map
# ──────────────────────────────────────────────
st.subheader("Map")

fig_map = px.scatter_mapbox(
    df_filtered,
    lat="lat",
    lon="lon",
    color="amenity",
    hover_name="primary_name" if "primary_name" in df_filtered.columns else None,
    hover_data=["amenity", "cuisine_clean"],
    mapbox_style=map_style,
    zoom=11,
    height=500,
    opacity=0.7,
)
fig_map.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig_map, use_container_width=True)

# ──────────────────────────────────────────────
# Charts
# ──────────────────────────────────────────────
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Amenity Distribution")
    amenity_counts = df_filtered["amenity"].value_counts().head(15)
    fig_bar = px.bar(
        x=amenity_counts.values,
        y=amenity_counts.index,
        orientation="h",
        labels={"x": "Count", "y": "Amenity Type"},
    )
    fig_bar.update_layout(height=400, yaxis={"autorange": "reversed"})
    st.plotly_chart(fig_bar, use_container_width=True)

with chart_col2:
    st.subheader("Top Cuisines")
    if "cuisine_clean" in df_filtered.columns:
        cuisine_counts = (
            df_filtered[df_filtered["cuisine_clean"] != "Unknown"]["cuisine_clean"]
            .value_counts()
            .head(10)
        )
        fig_cuisine = px.bar(
            x=cuisine_counts.values,
            y=cuisine_counts.index,
            orientation="h",
            labels={"x": "Count", "y": "Cuisine"},
        )
        fig_cuisine.update_layout(height=400, yaxis={"autorange": "reversed"})
        st.plotly_chart(fig_cuisine, use_container_width=True)
    else:
        st.info("No cuisine data available")

# ──────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "Data source: [OpenStreetMap](https://www.openstreetmap.org/copyright) via "
    "[Overpass API](https://overpass-api.de/) · "
    "Built with [Streamlit](https://streamlit.io/)"
)
