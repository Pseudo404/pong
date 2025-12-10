# 🏓 Pong.py

**Pong.py** est un jeu de type **Pong** développé en Python avec `pygame`.  
Il s’agit de **mon troisième jeu** et d’un projet personnel réalisé en **2023**, soit **un an après mon premier projet**, pendant ma période d’apprentissage autonome avant mon entrée dans l’enseignement supérieur.

Depuis sa création, le projet n’a reçu qu’une seule modification notable :  
👉 l’amélioration de la **fluidité des déplacements**, une notion que je ne maîtrisais pas encore à l’époque.

---

## 🧠 Contexte du projet

Lors de la création de ce jeu :
- J’avais déjà réalisé plusieurs petits projets en Python
- Je commençais à mieux comprendre la logique de jeu et la gestion des collisions
- Je ne maîtrisais pas encore correctement la notion de **delta time** et de mouvements fluides

Ce projet marque une **progression claire** par rapport à mes jeux précédents, notamment en termes de :
- structure du code
- gestion du temps
- interactions entre entités (joueurs / balle)

Aujourd’hui, en **1ʳᵉ année de Bachelor Développeur**, ce projet illustre bien mon évolution technique entre mes débuts et ma formation actuelle.

---

## 🎮 Principe du jeu

Le jeu reprend les bases classiques du **Pong** :
- Deux joueurs contrôlent chacun une raquette
- Une balle rebondit sur les murs et les raquettes
- Un point est attribué lorsqu’un joueur ne parvient pas à renvoyer la balle
- La vitesse de la balle augmente progressivement avec le temps

Des informations sont affichées à l’écran :
- Score des deux joueurs
- Temps écoulé
- Vitesse de la balle

---

## 🛠️ Technologies utilisées

- **Langage** : Python
- **Librairies** :
  - `pygame`
  - `time` (bibliothèque standard)
  - `random` (bibliothèque standard)
- **Concepts abordés** :
  - Programmation orientée objet (classes `J1`, `J2`, `Ball`)
  - Gestion des événements clavier
  - Collisions (`rect.colliderect`)
  - Gestion du temps et accélération progressive
  - Affichage 2D et interface simple avec `pygame`
  - Gestion d’un score et d’un timer

---

## ▶️ Lancer le projet

Prérequis :
- **Python 3**
- La librairie `pygame`
- Les fichiers d’images nécessaires (`j1.png`, `j2.png`, `ball.png`)

Installation de la dépendance :

```bash
pip install pygame
