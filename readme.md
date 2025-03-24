# Application de Reconnaissance Faciale avec PCA

## Description

Cette application utilise l'analyse en composantes principales (PCA) pour effectuer la reconnaissance faciale. Elle est développée en utilisant le framework Django.

## Fonctionnalités

- Chargement des images faciales
- Prétraitement des images
- Application de PCA pour la réduction de dimensionnalité
- Reconnaissance faciale basée sur les composantes principales

## Prérequis

- Python 3.x
- Django
- NumPy
- OpenCV
- Scikit-learn
- Voir le reste dans le fichier 'requirements.txt'

## Installation

1. Clonez le dépôt :

    ```bash
        git clone https://github.com/Devstyno/pca_django_app.git
    ```

2. Accédez au répertoire du projet :

    ```bash
        cd reconnaissance_faciale_avec_pca
    ```

3. Installez les dépendances :

    ```bash
        pip install -r requirements.txt
    ```

## Utilisation

1. Démarrez le serveur Django :

    ```bash
        python manage.py runserver
    ```

2. Accédez à l'application via votre navigateur à l'adresse `http://127.0.0.1:8000`.

## Structure du Projet

- `pca_reco_facial/` : Contient les fichiers de l'application Django
- `static/` : Contient les fichiers statiques (CSS, JavaScript, images)
- `templates/` : Contient les templates HTML
- `manage.py` : Script de gestion de Django

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Auteur

- [Yao David SOUSSOUKPO](https://github.com/devstyno)
