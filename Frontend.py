# -*- coding: utf-8 -*-
"""
Created on Mon May  5 10:46:26 2025

@author: hanschulzeerde
"""

# app.py

import streamlit as st
import pandas as pd
from Green_Robo_Advisor_main import run_robo_advisor

st.set_page_config(page_title="Green Robo Advisor", layout="centered")
st.title("🌱 Green Robo Advisor")

st.markdown("Erstelle dein nachhaltiges ETF-Portfolio basierend auf deinem Risikoprofil.")

# Seitenleiste – Eingaben
st.sidebar.header("⚙️ Einstellungen")
risk = st.sidebar.slider("Risikoneigung (1 = gering, 5 = hoch)", 1, 5, 3)
amount = st.sidebar.number_input("Anlagebetrag (€)", min_value=1000, step=500, value=10000)
sri = st.sidebar.selectbox("Nachhaltigkeitsstil", ["ESG", "SRI", "Impact"])

# Berechnung starten
if st.sidebar.button("📊 Portfolio berechnen"):
    result = run_robo_advisor(risk, amount, sri)

    st.subheader("📈 Ergebnis")
    st.write(f"**Erwartete Rendite:** {result['expected_return']:.2%}")
    st.write(f"**Risiko (Volatilität):** {result['risk']:.2%}")

    weights_df = pd.DataFrame.from_dict(result["weights"], orient='index', columns=["Gewichtung"])
    weights_df.index.name = "ETF"
    st.dataframe(weights_df.style.format({"Gewichtung": "{:.2%}"}))
    st.bar_chart(weights_df)

    csv = weights_df.to_csv().encode("utf-8")
    st.download_button("⬇️ Download CSV", csv, "portfolio.csv", "text/csv")
else:
    st.info("Bitte gib deine Daten ein und klicke auf 'Portfolio berechnen'.")
