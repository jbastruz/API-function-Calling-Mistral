# API-function-Calling-Mistral

**API en FastAPI et notebook de démonstration pour appeler dynamiquement des fonctions Python via Mistral AI.**

## 🚀 Description

Ce projet propose une API et un notebook de démonstration pour la *Function Calling* avec Mistral, permettant :

- d'intégrer Mistral.ai (modèle LLM) à l'exécution de fonctions Python
- de dialoguer en langage naturel pour déclencher des appels de fonctions
- d'exposer et tester ces fonctionnalités via une API FastAPI et via Jupyter

## 🛠️ Fonctionnalités

- Serveur FastAPI pour exposer des endpoints fonctionnels
- Notebook explicatif pour l'utilisation de Mistral avec la function calling
- Exemples d'appels de fonctions variées : parsing, interaction avec des fichiers, etc.
- Documentation interactive via Swagger UI (`/docs`)

## 📦 Structure du projet

- `FastAPI.py` : Serveur API principal
- `Mistral function Calling.ipynb` : Démonstration intégrée en notebook
- `items.csv` : Exemple de données pour manipulations fonctionnelles
- `.gitignore` : Config git standard
- `README.md` : Ce fichier de présentation

## 🧰 Packages requis

- `pandas`
- `requests`
- `functools`
- `json`
- `mistralai`
- `fastapi` et `uvicorn` (pour lancer le serveur API)

Installez les dépendances avec :
```bash
pip install pandas requests functools json mistralai fastapi uvicorn
```

## 🔑 Clé API Mistral

Le projet nécessite la clé API Mistral, disponible sur https://console.mistral.ai.  
Définissez votre clé dans le code :

```python
api_key = "VOTRE_MISTRAL_API_KEY"
```

## 💡 Utilisation

1. Lancez l'API avec :
    ```bash
    uvicorn FastAPI:app --reload
    ```
   Swagger UI sera accessible à http://localhost:8000/docs

2. Ouvrez `Mistral function Calling.ipynb` pour parcourir et tester la fonction calling en interactif.

## 📄 Exemples

Le notebook montre comment construire une requête pour demander à Mistral d'exécuter une fonction Python selon l'intention détectée dans le texte.

## 🏗️ Contributions

Suggestions, corrections, ou extensions — toute contribution est la bienvenue !

---
