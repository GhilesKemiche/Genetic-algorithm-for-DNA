# ST2 (Théorie des Jeux) - EI Algorithmique Génétique

![CentraleSupelec Logo](https://www.centralesupelec.fr/sites/all/themes/cs_theme/medias/common/images/intro/logo_nouveau.jpg)


## Introduction au code ##

Nous allons étudier des séquences d'ADN à partir de leur trajectoire tri-dimensionnelle. Plus précisèment, l'objectif de ce projet est de modifier le modèle de conformation 3D donné afin de rendre un plasmide circulaire. Nous allons utiliser 2 méthodes distinctes pour cela: le Recuit simulé et l'Algorithme génétique. Ainsi nous comparerons leurs performances.



**Pour lancer le programme, exécutez pour l'algo génetique: python -m dna .\data\plasmid_8k.fasta AG (pour recuit: python -m dna .\data\plasmid_8k.fasta RC)**


## Sprints ##

 - Definition des objectifs
 - Organisation du groupe
 - Planification
 - Code Recuit
 - Validation Recuit
 - Code AG
 - Validation AG
 - Comparaison


## Feuille de route :

- Lundi: Définition des objectifs, organisation du travail, code de recuit simulé
- Mardi: Fin du code rcuit simulé et validation
- Mercredi: Fin validation recuit et code AG
- Jeudi: fin code et validation AG, comparaisons
- Vendredi: bilan du travail


## Fonctionnalités :

- Recuit simulé
- Algorithme génétique

## Gitlab :

https://github.com/GhilesKemiche/Genetic-algorithm-for-DNA

## Bienvenue au repository du groupe:

Le Groupe :

* Mehdi Kalla
* Ghiles Kemiche
* Abiram Subramaniam
* Maxime Pilorget


## Packages utilisés :

```
pip install mathutils
pip install numpy
pip install matplotlib
pip install random
pip install tqdm
pip install pytest
pip install copy
pip install time

```




## Ressources

Sont fournis :

- le fichier <tt>Traj3D.py</tt> implémentant le moteur de calcul d'une trajectoire 3D,
- le fichier <tt>Rot_Table.py</tt> contenant la table de rotations (avec les écart-types) nécessaires au calcul d'une trajectoire 3D,
- le fichier <tt>Main.py</tt> illustrant un exemple d'utilisation de la classe Traj3D,
- deux fichiers <tt>.fasta</tt> contenant les séquences de deux plasmides de longueur différente (8 000 dans un cas et 180 000 dans l'autre).
- Exécution : <code>python -m 3dna --help</code>

