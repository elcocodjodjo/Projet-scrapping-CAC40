import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import os
import gc

rapport_path = "rapport_quotidien.txt"
if os.path.exists(rapport_path):
    with open(rapport_path, "r") as f:
        rapport_texte = f.read()
else:
    rapport_texte = "Le rapport quotidien n'est pas encore disponible."

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Tableau de bord des prix EUR/USD", style={'textAlign': 'center'}),
   
    html.H2(id='latest-rate', style={'textAlign': 'center', 'color': 'gray'}),


    # Rafraîchissement automatique toutes les 5 min
    dcc.Interval(
        id='interval-component',
        interval=5 * 60 * 1000,
        n_intervals=0
    ),

    dcc.Graph(id='prix-eur-usd-graph'),

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
    ]),
])

@app.callback(
    [Output('prix-eur-usd-graph', 'figure'),
     Output('latest-rate', 'children')],
    Input('interval-component', 'n_intervals')
)


def update_content(n):
    print(f"[Callback] Rafraîchissement {n}")
    gc.collect()

    try:
        df = pd.read_csv("prix_eur_usd.csv", header=None, engine='python')
        df.columns = ['Date', 'Price']
        df['Date'] = pd.to_datetime(df['Date'])
    except Exception as e:
        print("[Erreur] Lecture CSV :", e)
        return dash.no_update, dash.no_update

    # Graphique
    fig = px.line(df.sort_values('Date'), x='Date', y='Price', title='Prix EUR/USD au fil du temps')

    # Dernier taux
    dernier = df.sort_values('Date').iloc[-1]
    taux_text = f"1 euro vaut {dernier['Price']:.4f} dollars"

    return fig, taux_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
