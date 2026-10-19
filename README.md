# Sauce Demo : tests automatisés avec Selenium et pytest

Projet d'automatisation de tests QA sur le site de démonstration [Sauce Demo](https://www.saucedemo.com), un faux magasin en ligne conçu pour s'entraîner aux tests.

## Technologies

- Python 3.12
- Selenium WebDriver
- pytest (fixtures, parametrize)
- pytest-html (rapports)

## Scénarios testés

| Fonctionnalité | Cas de test | Résultat attendu |
|---|---|---|
| Connexion | Titre de la page de login | Le titre est « Swag Labs » |
| Connexion | Identifiants valides | Accès à la page « Products » |
| Connexion | Mauvais mot de passe | Message d'erreur affiché |
| Connexion | Nom d'utilisateur vide | Message « Username is required » |
| Connexion | Mot de passe vide | Message « Password is required » |
| Connexion | Utilisateur bloqué | Message « locked out » |
| Panier | Ajout d'un produit | Le compteur du panier affiche 1 |

## Structure du projet

```
├── tests/          # Fichiers de tests
├── pages/          # Page Objects (à venir)
├── conftest.py     # Fixtures partagées (driver, utilisateur connecté)
├── pytest.ini      # Configuration de pytest
└── requirements.txt
```

## Lancer les tests

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m pytest
```

Google Chrome doit être installé.

## Bonnes pratiques appliquées

- Attentes explicites (`WebDriverWait`) plutôt que `time.sleep`
- Fixtures pytest pour ouvrir et fermer le navigateur
- Tests pilotés par les données (`parametrize`) pour les cas d'erreur de connexion

## À venir

- Page Object Model
- Tests du checkout et du tri des produits
- Rapport HTML
- Intégration continue avec GitHub Actions