
# Analyse de la Performance du Département de Santé

Ce projet analyse la performance du département de santé dans une compagnie d'assurance pour l'année 2023. En raison du manque de données publiques appropriées, des données synthétiques ont été générées pour créer un ensemble de données réaliste.

## Vue d'Ensemble du Projet

Le projet suit ces étapes :

1. **Génération de Données** :
   - Les données synthétiques ont été générées à l'aide de `GenData2023.py`.
   - Les données générées sont stockées dans `data_table2023.csv`.

2. **Préparation des Données** :
   - Le fichier CSV a été téléchargé dans une base de données MySQL.
   - Le nettoyage et la préparation des données ont été effectués en utilisant SQL, avec le code disponible dans `DATA CLEANING.sql`.
   - Les données nettoyées ont été téléchargées sous forme de `DT_prepared.csv`.

3. **Analyse des Données** :
   - Plusieurs questions clés ont été répondues sur la base des données préparées :
     - Quel est le nombre total de déclarations en 2023 ?
     - Quelle est la somme des frais engagés en 2023 ?
     - Quel est le frais moyen par déclaration ?
     - Quel est le total des frais engagés par mois ?
     - etc ...

4. **Visualisation des Données** :
   - Les résultats de l'analyse ont été visualisés dans un rapport Power BI, `Report2023.pbix`.

5. **Automatisation** :
   - Le script Python `Extract.py` automatise les étapes de génération et de préparation des données.

## Structure du Projet

- `GenData2023.py` : Script pour générer des données synthétiques.
- `data_table2023.csv` : Données synthétiques générées.
- `DATA CLEANING.sql` : Script SQL pour le nettoyage et la préparation des données.
- `DT_prepared.csv` : Données nettoyées et préparées.
- `Report2023.pbix` : Rapport Power BI pour la visualisation des données.
- `Extract.py` : Script Python pour automatiser la génération et la préparation des données.

## Technologies
- Python
- SQL
- Power BI
- MySQL

## Installation et Utilisation

### Prérequis

- Python 3.x
- Serveur MySQL
- Power BI Desktop

### Installation

1. **Cloner le dépôt** :
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Installer les dépendances Python** :
    ```sh
    pip install -r requirements.txt
    ```

3. **Exécuter le script de génération de données** :
    ```sh
    python GenData2023.py
    ```

4. **Télécharger le CSV dans MySQL** :
    - Utilisez votre méthode préférée pour télécharger `data_table2023.csv` dans une base de données MySQL.

5. **Exécuter le script SQL pour nettoyer et préparer les données** :
    - Exécutez les commandes dans `DATA CLEANING.sql` dans votre base de données MySQL.

6. **Télécharger les données préparées** :
    - Exportez le résultat sous forme de `DT_prepared.csv`.

7. **Générer le rapport Power BI** :
    - Ouvrez `Report2023.pbix` dans Power BI Desktop pour voir les visualisations.

### Automatisation

- Pour automatiser les étapes de génération et de préparation des données, exécutez :
    ```sh
    python Extract.py
    ```

## Contributeurs

- Melik Soufiane

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
