# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:51:56 2025

@author: cypri
"""
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import os

rapport_path = "rapport_quotidien.txt"
if os.path.exists(rapport_path):
    with open(rapport_path, "r") as f:
        rapport_texte = f.read()
else:
    rapport_texte = "Le rapport quotidien n'est pas encore disponible."

# Lire le fichier CSV avec header=None, car il semble ne pas avoir de ligne d'en-tête
df = pd.read_csv('prix_eur_usd.csv', header=None)

# Afficher les premières lignes pour vérifier la structure des données
print(df.head())

# Ajouter les noms de colonnes manuellement
df.columns = ['Date', 'Price']

# Vérifier les noms des colonnes
print(df.columns)

# Assurez-vous que la colonne 'Date' est bien au format datetime
df['Date'] = pd.to_datetime(df['Date'])

# Vérifier que les données sont correctes
print(df.head())

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Créer un graphique à partir des données du CSV
fig = px.line(df, x='Date', y='Price', title='Prix EUR/USD au fil du temps')

df_table = df.sort_values("Date", ascending =False)

# Mettre en place la mise en page du tableau de bord
app.layout = html.Div([
    html.H1("Tableau de bord des prix EUR/USD", style={'textAlign': 'center'}),
    dcc.Graph(
        id='prix-eur-usd-graph',
        figure=fig
    ),
    html.Div([
        html.H4("Données CSV", style={'textAlign': 'center'}),
        html.Table([
            html.Tr([html.Th(col) for col in df_table.columns])  # En-têtes du tableau
        ] + [
            html.Tr([html.Td(df_table.iloc[i][col]) for col in df_table.columns]) for i in range(len(df))
        ], style={'margin': '20px auto', 'borderCollapse': 'collapse', 'width': '80%'})
    ])
    html.Div([
        html.H4("📈 Rapport quotidien (20h)", style={'textAlign': 'center'}),
        html.Pre(rapport_texte, style={
            'backgroundColor': '#f9f9f9',
            'padding': '10px',
            'whiteSpace': 'pre-wrap',
            'border': '1px solid #ccc',
            'width': '80%',
            'margin': 'auto'
        })
    ])
])

# Lancer le serveur avec `app.run()` au lieu de `app.run_server()`
if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8050, debug=True)
