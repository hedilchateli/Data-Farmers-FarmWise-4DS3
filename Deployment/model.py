# model.py
import pickle
import pandas as pd
import time
import logging
import os

# Configure les logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

MODEL_FILENAME = 'best_model.pkl'
model = None
scaler = None

def load_model():
    global model, scaler
    logger.info("Début chargement du modèle et du scaler...")
    start_time = time.time()

    if not os.path.exists(MODEL_FILENAME):
        logger.warning(f"⚠️ Le fichier '{MODEL_FILENAME}' est introuvable. Mode prédiction désactivé.")
        return False

    with open(MODEL_FILENAME, 'rb') as f:
        data = pickle.load(f)

    model = data['model']
    scaler = data['scaler']

    logger.info(f"✅ Modèle et scaler chargés en {time.time() - start_time:.2f} secondes")
    return True

# Charger automatiquement au démarrage
load_model()

def predict_price(input_data: dict) -> float:
    if model is None:
        raise Exception("Modèle non chargé. Impossible de faire une prédiction.")

    features = [
        'region_encoded',
        'Surface(m2)',
        'Proximiteplage',
        'TitreFoncier',
        'EauDisponible',
        'electricite',
        'Cloture',
        'NbArbres',
        'TypedeCulture',
        'Irrigation',
        'batiment',
        'route'
    ]

    X = pd.DataFrame([[input_data[feat] for feat in features]], columns=features)

    logger.info(f"🚀 Données reçues pour la prédiction :\n{X}")

    # ⚡ PAS de scaling ici car entraînement sur X non-scalé
    prediction = model.predict(X)[0]
    logger.info(f"🎯 Prix prédit : {prediction}")

    return prediction
