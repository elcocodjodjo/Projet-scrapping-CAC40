#!/bin/bash

# URL du site
url="https://forex.tradingsat.com/cours-euro-dollar-FX0000EURUSD/"

# Fichier CSV où seront stockées les données
output_file="/home/delplacecharlie/Projet-scrapping-CAC40/prix_eur_usd.csv"

# Ajouter l'en-tête au fichier CSV si c'est la première exécution
if [ ! -f "$output_file" ]; then
    echo "Date,Price" > "$output_file"
fi

# Récupérer le prix avec curl et grep
price=$(curl -s "$url" | grep -oP '(?<=<span class="price">)[^<]+')

# Récupérer la date/heure actuelle
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Ajouter la ligne dans le fichier CSV
echo "$timestamp,$price" >> "$output_file"

