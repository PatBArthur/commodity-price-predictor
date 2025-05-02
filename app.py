import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

# Load and display data
@st.cache_data
def load_data():
    prices = pd.read_csv("commodity_prices_cleaned.csv", parse_dates=["Date"])
    returns = pd.read_csv("commodity_returns.csv", parse_dates=["Date"])
    return prices, returns

prices, returns = load_data()

# Target variable (Gold up/down)
if "Gold" in returns.columns:
    returns["Target"] = (returns["Gold"].shift(-1) > 0).astype(int)
    returns.dropna(inplace=True)
else:
    st.error("'Gold' column is missing from returns.csv")
    st.stop()

# Log dataset size for debugging
st.write(f"Returns shape after shift/drop: {returns.shape}")

# Ensure minimum data to train
if returns.shape[0] < 5:
    st.error("Not enough data points after processing. Please add more historical return data.")
    st.stop()

X = returns.drop(columns=["Date", "Target"])
y = returns["Target"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)

# UI
st.title("Commodity Price Movement Predictor")

st.header("📈 Commodity Price Trends")
selected = st.multiselect("Select commodities:", options=prices.columns[1:], default=["Gold", "Silver"])
fig, ax = plt.subplots(figsize=(12, 4))
for col in selected:
    ax.plot(prices["Date"], prices[col], label=col)
ax.legend()
ax.set_title("Prices 2015–2025")
st.pyplot(fig)

st.header("🔗 Return Correlation")
corr = returns.drop(columns=["Date", "Target"]).corr()
fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
ax2.set_title("Correlation of Returns")
st.pyplot(fig2)

st.header("📊 Feature Importance")
st.bar_chart(importances)

st.header("🤖 Predict Tomorrow's Gold Movement")
custom_inputs = []
st.write("Enter today’s returns for each commodity (%):")
for col in X.columns:
    val = st.slider(f"{col}", -5.0, 5.0, 0.0, 0.1)
    custom_inputs.append(val / 100)

if st.button("Predict"):
    prediction = model.predict([custom_inputs])[0]
    st.success("📈 Gold will go UP" if prediction == 1 else "📉 Gold will go DOWN")