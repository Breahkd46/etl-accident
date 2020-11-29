# etl-accident

Ce projet a pour but de construire un entrepot de données 
autour des accidents corporel de a la route. Nous avons pensez 
cet entrepot selon 4 dimensions : 
* geographique
* condition météorologique
* type de personne
* type de vehicule

Le programme ecrit en python est le prossecus d'ETL de 
l'entrepot de données.
## Pre-requis
* docker 
* python 3.8
* pip

## Structure
raw
4 fichier principaux : 
* etl_accidnet.py permet de lancé le programme 
de création de données et le processus d'ETL
* extract.py permet de d'extraire les données 
depuis le site du gouvernement francais
* transform.py permet de transformer les données 
pour pouvoir les insérer dans a base de données 
selon le schema présenté dans le dossier doc.
* load.py permet de charger les données dans 
une base de données PostrgreSQL   

## Lancer l'application

#### Lancer la base de données

>`docker-compose up`

#### Lancer l'ETL

>`pip install -r requirements.txt`
>
>`python src/etl_accident.py`

## Schema

![Schema sql](https://github.com/Breahkd46/etl-accident/blob/master/doc/etl_accident.png "Schema sql")
