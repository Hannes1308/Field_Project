# -*- coding: utf-8 -*-
"""
Created on Mon May  5 12:32:50 2025

@author: hanschulzeerde
"""

# app.py

import streamlit as st
import pandas as pd
from Green_Robo_Advisor_main import run_robo_advisor

st.set_page_config(page_title="Green Robo Advisor", layout="centered")
st.title("🌱 Green Robo Advisor")

st.markdown("Stelle dir dein nachhaltiges ETF-Portfolio zusammen.")

# Eingabemaske in der Seitenleiste
st.sidebar.header("⚙️ Einstellungen")
risk = st.sidebar.slider("Risikoneigung (1 = niedrig, 5 = hoch)", 1, 5, 3)
amount = st.sidebar.number_input("Anlagebetrag (€)", min_value=1000, step=500, value=10000)
sri_type = st.sidebar.selectbox("Nachhaltigkeitsstil", ["ESG", "SRI", "Impact"])

# Berechnung starten
if st.sidebar.button("📊 Portfolio berechnen"):
    result = run_robo_advisor(risk, amount, sri_type)

    if "error" in result:
        st.error(result["error"])
    else:
        st.subheader("📈 Ergebnis")
        st.write(f"**Erwartete Rendite:** {result['expected_return']:.2%}")
        st.write(f"**Risiko (Volatilität):** {result['risk']:.2%}")

        df = pd.DataFrame.from_dict(result["weights"], orient="index", columns=["Gewichtung"])
        df.index.name = "ETF"
        st.dataframe(df.style.format({"Gewichtung": "{:.2%}"}))
        st.bar_chart(df)

        csv = df.to_csv().encode("utf-8")
        st.download_button("⬇️ CSV herunterladen", csv, "portfolio.csv", "text/csv")
else:
    st.info("Bitte gib deine Einstellungen ein und klicke auf „Portfolio berechnen“.")
