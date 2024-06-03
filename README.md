
# Report 2023

## Description
Ce projet implique la génération de données synthétiques, leur nettoyage, et la création de tableaux de bord avec Power BI. De plus, il automatise le processus d'extraction et de nettoyage des données.

## Table des Matières
- [Description](#description)
- [Fichiers](#fichiers)
- [Technologies](#technologies)
- [Installation et Utilisation](#installation-et-utilisation)
- [Flux de Travail du Projet](#flux-de-travail-du-projet)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Fichiers
- `GenData2023.py`: Script pour générer des données synthétiques.
- `data_table2023.csv`: Données synthétiques générées.
- `Data_Cleaning.sql`: Script SQL pour le nettoyage des données (suppression des doublons, standardisation des données).
- `DT_prepared.csv`: Données nettoyées téléchargées depuis le serveur MySQL.
- `Report2023.pbix`: Rapport Power BI créé à partir de `DT_prepared.csv`.
- `Extract.py`: Script pour automatiser l'extraction et le nettoyage des données.

## Technologies
- Python
- SQL
- Power BI
- MySQL

## Installation et Utilisation

### Générer des Données Synthétiques
```bash
python GenData2023.py
```

### Nettoyer les Données
1. Charger `Data_Cleaning.sql` dans votre serveur MySQL et l'exécuter pour nettoyer `data_table2023.csv`.
2. Télécharger les données nettoyées sous forme de `DT_prepared.csv`.

### Créer des Tableaux de Bord
1. Ouvrir `Report2023.pbix` avec Power BI Desktop.
2. Actualiser les données pour s'assurer qu'elles reflètent bien `DT_prepared.csv`.

### Automatiser l'Extraction et le Nettoyage des Données
```bash
python Extract.py
```

## Flux de Travail du Projet
1. Générer des données synthétiques avec `GenData2023.py`.
2. Nettoyer les données avec `Data_Cleaning.sql`.
3. Télécharger les données nettoyées sous forme de `DT_prepared.csv`.
4. Créer des tableaux de bord Power BI avec `DT_prepared.csv` et les enregistrer sous forme de `Report2023.pbix`.
5. Automatiser l'extraction et le nettoyage avec `Extract.py`.

## Contribuer
Les contributions sont les bienvenues ! Veuillez cloner ce dépôt et soumettre des pull requests.

## Licence
Ce projet est sous licence MIT.
