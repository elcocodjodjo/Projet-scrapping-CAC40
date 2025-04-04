# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:51:56 2025

@author: cypri
"""
import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

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
            html.Tr([html.Th(col) for col in df.columns])  # En-têtes du tableau
        ] + [
            html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(len(df))
        ], style={'margin': '20px auto', 'borderCollapse': 'collapse', 'width': '80%'})
    ])
])

# Lancer le serveur avec `app.run()` au lieu de `app.run_server()`
if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8050, debug=True)
