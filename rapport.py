import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Charger les données
df = pd.read_csv("prix_eur_usd.csv", names=["Date", "Price"], skiprows=1)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Heure actuelle
now = datetime.now()

# Si on est avant 20h, analyser la période de avant-hier 20h à hier 20h
if now.hour < 20:
    start = (now - timedelta(days=2)).replace(hour=20, minute=0, second=0, microsecond=0)
    end = (now - timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0)
    date_rapport = (now - timedelta(days=1)).date()
else:
    # Sinon on analyse hier 20h → aujourd’hui 20h
    start = (now - timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0)
    end = now.replace(hour=20, minute=0, second=0, microsecond=0)
    date_rapport = now.date()

# Sélection de la période
df_period = df[(df["Date"] >= start) & (df["Date"] <= end)]

# Calculs
min_price = df_period["Price"].min()
max_price = df_period["Price"].max()
df_period.loc[:, "log_return"] = np.log(df_period["Price"] / df_period["Price"].shift(1))
volatility = df_period["log_return"].std()

# Écriture du rapport
with open("rapport_quotidien.txt", "w") as f:
    f.write(f"Rapport du {date_rapport.strftime('%Y-%m-%d')}\n")
    f.write(f"Prix minimum (20h-20h) : {min_price:.4f}\n")
    f.write(f"Prix maximum (20h-20h) : {max_price:.4f}\n")
    f.write(f"Volatilité : {volatility:.6f}\n")
