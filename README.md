# Projet-scrapping-CAC40
Objectif du projet:
L’objectif de ce projet est de construire un pipeline complet de scraping automatisé d’un site web dynamique, et d’afficher en temps réel les données récoltées sur un dashboard interactif développé avec Dash en Python. Le projet inclut :

Une extraction régulière des données via un script Bash.

Le stockage en série temporelle de ces données dans un fichier .csv.

Un dashboard contenant :

La valeur actuelle de la donnée.

Un graphique dynamique retraçant l’évolution au cours du temps.

Un rapport journalier généré chaque soir à 20h (statistiques, résumé…).

Une mise à jour automatique via cron toutes les 5 minutes.

🌍 Site web choisi:
Nous avons choisi de suivre l’évolution de la parité euro/dollar (EUR/USD) sur le site :

🔗 https://forex.tradingsat.com/cours-euro-dollar-FX0000EURUSD/

Ce site a l’avantage de proposer une structure HTML stable et permet d’accéder à la donnée de manière fiable.

🔧 Pourquoi ce site ?
Nous avons initialement tenté de récupérer les données à partir de sites comme Barchart, Investing.com, ou TradingView, mais nous avons rencontré de nombreuses limitations techniques :

Blocage de requêtes non-authentifiées (403 Forbidden).

Chargement des données via JavaScript dynamique, rendant le scraping Bash impossible.

Protection contre les bots et taux de rafraîchissement très élevé.

Le site tradingsat.com s’est révélé être un bon compromis, avec une donnée accessible directement dans le HTML.

⚙️ Méthodologie
1. 📥 Scraping avec Bash
Nous avons utilisé curl et grep dans un script bash (scrape.sh) pour extraire la parité EUR/USD. Exemple simplifié de la commande utilisée :

bash
Copier
Modifier
curl -s "https://forex.tradingsat.com/cours-euro-dollar-FX0000EURUSD/" | grep ...
La donnée est ensuite formatée et ajoutée avec timestamp dans un fichier prix_eur_usd.csv.

2. 📈 Visualisation avec Dash (Python)
Nous avons construit une interface avec le framework Dash qui permet :

L’affichage de la dernière parité EUR/USD scrappée.

Un graphique dynamique (utilisant Plotly) affichant l’évolution depuis le lancement du projet.

Un rapport journalier (mis à jour chaque jour à 20h via cron) affichant :

Écart-type ( Volatilité de la parité EUR/DOL)

Valeur min/max du jour

3. 🕒 Automatisation avec Cron
Deux tâches cron sont planifiées :

⏱️ Toutes les 5 minutes : exécution du script de scraping et mise à jour du data.csv.

📅 Chaque jour à 20h : génération du rapport statistique.

📁 Arborescence du projet
///venv
///.gitignore
///README.md
///grep.sh
///main.py
///prix_eur_usd.csv
///scrapper.py
///scrapper.sh

💼 Répartition du travail:
CYPRIEN DUCEUX: Choix et test du site internet 

Extraction des donnés dash

Création du fichier CSV

ALgorithme Python pour le Dash Bord

CHARLIE DELPLACE: Automatisation avec cron 

Implémentation de la machine virtuelle

ALgorithme Python pour le Dash Bord


✨ Conclusion
Ce projet nous a permis de maîtriser un workflow complet alliant Bash, Python, gestion de cron, visualisation avec Dash, et traitement de données. 
Malgrès les difficultés rencontrées notamment dans l'extraction des données, nous avons trouvé le projet passionant et très formateur.
