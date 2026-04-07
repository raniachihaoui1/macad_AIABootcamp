# 🚀 Exercise 06 — Build Your Streamlit App

**Day 3 · Open-ended**

No starter code. You've written all the pieces in Exercises 01–04 — now assemble them into a web app.

---

### What is Streamlit?

A Python script → a web app. No HTML/CSS/JS. Widgets are one-liners, charts from matplotlib/plotly work directly, `@st.cache_data` prevents re-loading.

---

### Your task

Edit `app.py` in the repo root. Use the skeleton template or start from scratch.

#### Minimum requirements

Your app must include:

- [ ] **A title** with your city name
- [ ] **At least one filter widget** (e.g. `st.selectbox` or `st.multiselect` to filter by amenity type)
- [ ] **An interactive map** showing amenities (use plotly `scatter_mapbox`)
- [ ] **At least one chart** (bar chart, histogram, pie chart — your choice)
- [ ] **KPI metrics** — use `st.metric()` to show at least 2 numbers (e.g. total amenities, % with names)
- [ ] **Cached data loading** — use `@st.cache_data` so the app doesn't reload data on every click

#### Bonus

- [ ] Multiple filters (amenity type + cuisine + has opening hours)
- [ ] Two maps (all amenities + restaurants by cuisine)
- [ ] A data table with `st.dataframe()` showing raw data
- [ ] Color customization via sidebar
- [ ] Download button for cleaned data (`st.download_button`)

---

### `app.py` structure

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page config (must be first Streamlit command)
st.set_page_config(page_title="My City EDA", layout="wide")

# 2. Data loading (cached)
@st.cache_data
def load_data():
    df = pd.read_csv("data/clean_your_city.csv")
    # ... any normalization from Exercise 03 ...
    return df

df = load_data()

# 3. Sidebar — filters
st.sidebar.header("Filters")
selected = st.sidebar.multiselect("Amenity type", df["amenity"].unique())
# ... filter df based on selection ...

# 4. Main area — title, KPIs, charts, maps
st.title("🏙️ My City Amenities")

col1, col2 = st.columns(2)
col1.metric("Total", len(df))
col2.metric("Types", df["amenity"].nunique())

# ... your plotly map ...
# ... your charts ...
```

---

### Run locally

```bash
# From the repo root:
streamlit run app.py
```

This opens a browser tab at `http://localhost:8501`. The app auto-reloads when you save `app.py`.

---

### Key Streamlit functions

| Function | What it does | Example |
|----------|-------------|---------|
| `st.title()` | Big heading | `st.title("My App")` |
| `st.header()` / `st.subheader()` | Section headings | `st.header("Map")` |
| `st.metric()` | KPI card with number | `st.metric("Total", 1234)` |
| `st.columns(n)` | Side-by-side layout | `col1, col2 = st.columns(2)` |
| `st.sidebar.selectbox()` | Dropdown in sidebar | `st.sidebar.selectbox("Pick", options)` |
| `st.sidebar.multiselect()` | Multi-select in sidebar | `st.sidebar.multiselect("Pick", options)` |
| `st.plotly_chart(fig)` | Show plotly figure | `st.plotly_chart(fig, use_container_width=True)` |
| `st.pyplot(fig)` | Show matplotlib figure | `st.pyplot(fig)` |
| `st.dataframe(df)` | Interactive data table | `st.dataframe(df.head(50))` |
| `@st.cache_data` | Cache function result | Decorator on data loading function |

---

### Reference

- **Streamlit docs:** [docs.streamlit.io](https://docs.streamlit.io)
- **Reference app:** [`example/app_stockholm.py`](../example/app_stockholm.py) — see how it's done for Stockholm
- **Stockholm notebook:** [`example/stockholm_eda.ipynb`](../example/stockholm_eda.ipynb) — Section 3.1 explains the notebook → app translation

---

### 📦 Deploy

Once your app works locally:

1. Commit and push `app.py` to your fork
2. Follow the deployment guide: [`docs/deploy.md`](../docs/deploy.md)
3. Get your public URL
4. **Present it to the class!**

Your public URL is your portfolio piece. Ship it.
