# Commodity Price Movement Predictor

This project uses a Random Forest classifier to predict whether the price of **Gold** will go up or down tomorrow, based on today's returns of various commodities like oil, silver, corn, etc.

Built with **Streamlit**, **scikit-learn**, **pandas**, and **matplotlib**, and visualized through an interactive web UI.

---

## 🔧 Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/PatBArthur/commodity-price-predictor.git
cd commodity-price-predictor
```

### 2. Create and activate virtual environment (macOS/Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Then open your browser to: [http://localhost:8501](http://localhost:8501)

---

## 📁 Files Overview

- `app.py` — Main Streamlit application
- `commodity_prices_cleaned.csv` — Historical prices of various commodities
- `commodity_returns.csv` — Daily returns calculated from those prices

---

## 🧠 Features

- Visualize commodity price trends (2015–2025)
- Correlation heatmap of returns
- Feature importance ranking from Random Forest
- Interactive sliders to input today’s returns and predict tomorrow’s gold movement

---

## ✍️ Author

Created by **Burke Arthur** for an Advanced Financial Analytics personal project.

