# -*- coding: utf-8 -*-
"""
Created on Mon May  5 12:31:50 2025

@author: hanschulzeerde
"""

# Green_Robo_Advisor_main.py

import pandas as pd
import os

def run_robo_advisor(risk_level, amount, sri_type):
    """
    Liest ETF-Daten aus Excel, filtert nach SRI-Typ, berechnet gleichmäßiges Portfolio.
    """
    file_path = os.path.join(os.path.dirname(__file__), "Green ETF Selection.xlsx")

    try:
        df = pd.read_excel(file_path, engine="openpyxl")
    except Exception as e:
        return {
            "weights": {},
            "expected_return": 0.0,
            "risk": 0.0,
            "error": f"Fehler beim Laden der Excel-Datei: {e}"
        }

    # Filter nach Nachhaltigkeitsstil (z. B. ESG, SRI, Impact)
    filtered = df[df["SRI_Type"].str.upper() == sri_type.upper()]

    if filtered.empty:
        return {
            "weights": {},
            "expected_return": 0.0,
            "risk": 0.0,
            "error": f"Keine ETFs mit SRI-Typ '{sri_type}' gefunden."
        }

    n = len(filtered)
    weights = dict(zip(filtered["ETF_Name"], [1 / n] * n))

    expected_return = filtered["Expected_Return"].mean() if "Expected_Return" in filtered else 0.06
    risk = filtered["Volatility"].mean() if "Volatility" in filtered else 0.12

    return {
        "weights": weights,
        "expected_return": expected_return,
        "risk": risk
    }
