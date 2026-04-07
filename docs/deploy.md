# Deploy to Streamlit Community Cloud

Turn your `app.py` into a live web app with a public URL. Takes about 2 minutes.

## Prerequisites

- A GitHub account
- Your own **fork** of this repository (with your completed `app.py`)
- `requirements.txt` in the repo root (already provided)

## Step-by-Step

### 1. Fork the Repository

1. Go to [github.com/AECinCode/edu.eda](https://github.com/AECinCode/edu.eda)
2. Click **Fork** (top right)
3. This creates `github.com/YOUR_USERNAME/edu.eda`

### 2. Push Your Work

Make sure your completed `app.py` is committed and pushed to your fork:

```bash
git add app.py
git commit -m "feat: complete streamlit app for [your city]"
git push origin main
```

### 3. Connect Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **Sign in with GitHub**
3. Authorize Streamlit to access your repositories

### 4. Deploy

1. Click **New app**
2. Fill in:
   - **Repository**: `YOUR_USERNAME/edu.eda`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Click **Deploy!**

### 5. Wait ~1 Minute

Streamlit will:
- Clone your repo
- Install packages from `requirements.txt`
- Start your app

### 6. Get Your Public URL

Once deployed, you'll get a URL like:

```
https://your-username-edu-eda-app-xxxxx.streamlit.app
```

This is your **portfolio link** — share it, put it on your CV, show it in presentations.

## Updating Your App

Every time you push to `main`, Streamlit automatically redeploys. Just:

```bash
git add app.py
git commit -m "fix: update chart colors"
git push
```

The app updates within a minute.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "ModuleNotFoundError" | Make sure the package is in `requirements.txt` and push again |
| App crashes on load | Check the app logs in the Streamlit dashboard (bottom-right "Manage app" menu) |
| Data loading is slow | Use `@st.cache_data` on your data loading function |
| "Resource limits exceeded" | Your dataset might be too large — filter to fewer amenity types |
| App sleeps after inactivity | Free tier apps sleep after 7 days of no visits — just visit the URL to wake it up |

## App Sleep Policy

Free Streamlit Community Cloud apps go to sleep after 7 days without traffic. When someone visits the URL, it wakes up in ~30 seconds. To keep it always awake, visit it occasionally or share the link.
