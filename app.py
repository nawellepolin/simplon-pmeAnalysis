import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

# Étape 5 : Exploration statistique avec Pandas
données['ca'] = données['prix'] * données['qte']

# 5a : Moyenne et médiane du CA et du volume des ventes par produit
moyenne_ca = données.groupby('produit')['ca'].mean()
moyenne_qte = données.groupby('produit')['qte'].mean()
médiane_ca = données.groupby('produit')['ca'].median()
médiane_qte = données.groupby('produit')['qte'].median()

print('Moyenne CA par produit :\n', moyenne_ca)
print('Moyenne volume ventes par produit :\n', moyenne_qte)
print('Médiane CA par produit :\n', médiane_ca)
print('Médiane volume ventes par produit :\n', médiane_qte)

# 5b : Écart-type et variance du volume des ventes par produit
écart_type_qte = données.groupby('produit')['qte'].std()
variance_qte = données.groupby('produit')['qte'].var()

print('Écart-type volume ventes par produit :\n', écart_type_qte)
print('Variance volume ventes par produit :\n', variance_qte)

# Étape 6 : Produit le plus et moins vendu en Python natif (sans Pandas)
total_par_produit = {}

for index, ligne in données.iterrows():
    produit = ligne['produit']
    qte = ligne['qte']
    
    if produit not in total_par_produit:
        total_par_produit[produit] = 0
    
    total_par_produit[produit] = total_par_produit[produit] + qte

print('\nTotal des ventes par produit :', total_par_produit)
print('Produit le moins vendu :', min(total_par_produit, key=total_par_produit.get))
print('Produit le plus vendu :', max(total_par_produit, key=total_par_produit.get))

# Étape 7 : Graphiques des ventes et du CA par produit
graphique_ventes_produit = px.pie(données, values='qte', names='produit', title='Ventes par produit')
graphique_ventes_produit.write_html('ventes-par-produit.html')

graphique_ca_produit = px.pie(données, values='ca', names='produit', title='Chiffre d\'affaires par produit')
graphique_ca_produit.write_html('ca-par-produit.html')