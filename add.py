import streamlit as st
from predict import predict_match
import pandas as pd

st.set_page_config(page_title="Tippmix Predictor", layout="centered")
st.title("⚽ Tippmix Predictor")

st.markdown("Enter two team names (in English, e.g. 'Barcelona', 'Real Madrid').")

home_team = st.text_input("Home team name")
away_team = st.text_input("Away team name")

if st.button("🔍 Predict"):
    result = predict_match(home_team, away_team)
    st.subheader("📊 Predictions")
    for key, value in result.items():
        st.write(f"**{key}**: {value}")

    df = pd.DataFrame([result])
    st.download_button("📥 Download CSV", data=df.to_csv(index=False), file_name="tippmix_prediction.csv", mime="text/csv")
