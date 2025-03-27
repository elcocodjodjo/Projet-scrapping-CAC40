    # -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:52:50 2025

@author: cypri
"""

import selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuration de l'option pour ne pas ouvrir une fenêtre de navigateur
chrome_options = Options()
chrome_options.add_argument("--headless")  # Si tu veux pas voir la fenêtre du navigateur

# Initialisation du WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Ouvrir la page
driver.get('https://www.barchart.com/stocks/quotes/$SPX')

# Attendre que la page soit complètement chargée
time.sleep(5)  # Attends 5 secondes pour être sûr que tout est chargé

# Trouver le prix actuel du S&P 500
price_element = driver.find_element(By.XPATH, '//div[@class="last-price"]/span[@class="price"]')
price = price_element.text

# Fermer le navigateur
driver.quit()

# Sauvegarder le prix dans un fichier
with open('prix_spx.txt', 'w') as file:
    file.write(price)

print(f"Prix du S&P 500: {price}")
