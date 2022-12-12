# VR_LAN

## Versions

| Version       | Auteur        | Date       | Changements           |
| :------------ |:-------------:| ----------:| :-------------------- |
| 1.0           | K. Carrillo   | 03/12/2022 | Création.             |

## Table des matières

* Projet
* Compatibilité
* Installation
* TODO

## Projet

Ce projet a pour objectif de créer une plateforme web permettant d'afficher les résultats en temps réel des LAN VR, 
ainsi que de vendre les goodies et les billets liés à cet évènements.

Le projet est réalisé avec le Framework Django.

## Compatibilité

La plateforme sera compatible avec les supports mobiles et desktop, quel que soit le navigateur ou l'OS.

## Installation

Pour lancer l'application, lancer les containers:

> docker-compose up -d --build

Puis copier le package sphinxdoc mis à jour pour la version CPython 3.11 dans le container web:

> docker cp [path/du/packages] ecom_web:/usr/local/lib/python3.11/site-packages

Enfin, activer le serveur django dans le container:

> docker exec -it ecom_web bash

> cd src

> python3 manage.py runserver

## TODO

* Ajout de la gestion des cookies
* Ajout de la gestion du profil
* Ajout du ecommerce
* Ajout de la doc
* Ajout du SEO
