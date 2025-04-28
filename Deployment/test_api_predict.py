import requests

# 📍 URL de ton API FastAPI
url = "http://127.0.0.1:8000/api/predict/"

# 📍 Exemple d'input à envoyer
payload = {
    "region_encoded": 5,       # Remplacer selon ta région (ex: 5 = Sousse)
    "Surface_m2": 12000,       # 12000 m² de surface
    "Proximiteplage": 1,       # Oui, proche plage
    "TitreFoncier": 1,         # Oui, titre foncier
    "EauDisponible": 1,        # Oui, eau disponible
    "electricite": 1,          # Oui, électricité disponible
    "Cloture": 1,              # Oui, clôture présente
    "NbArbres": 100,           # 100 arbres
    "TypedeCulture": 2,        # 2 = Oliviers
    "Irrigation": 1,           # Oui, irrigation présente
    "batiment": 0,             # Pas de bâtiment
    "route": 1                # Route présente
}

# 📍 Envoyer la requête POST
response = requests.post(url, json=payload)

# 📍 Afficher la réponse
if response.status_code == 200:
    print("✅ Réponse de l'API :", response.json())
else:
    print(f"❌ Erreur {response.status_code} :", response.text)
