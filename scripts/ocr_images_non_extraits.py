import os
import pytesseract
from PIL import Image

# === CONFIGURATION ===
ERREURS_FILE = "data/erreurs.txt"
INPUT_DIR = "docs"
OUTPUT_DIR = "data/texts"
LANG = "fra"  # ou "eng"

# Vérifie le fichier d'erreurs
assert os.path.exists(ERREURS_FILE), "Fichier d'erreurs manquant"

# Charge les fichiers .jpg à traiter
with open(ERREURS_FILE, "r", encoding="utf-8") as f:
    lignes = f.readlines()

jpgs_a_traiter = [
    ligne.split(" — ")[0] for ligne in lignes
    if ligne.split(" — ")[0].lower().endswith(".jpg")
]
if not jpgs_a_traiter:
    print("✅ Aucun fichier JPG à traiter avec OCR.")
    exit()

# OCR sur chaque image
for jpg_name in jpgs_a_traiter:
    input_path = os.path.join(INPUT_DIR, jpg_name)
    base_name = os.path.splitext(jpg_name)[0]
    output_path = os.path.join(OUTPUT_DIR, base_name + ".txt")

    try:
        print(f"📸 OCR en cours : {jpg_name}")
        image = Image.open(input_path)
        texte = pytesseract.image_to_string(image, lang=LANG)

        with open(output_path, "w", encoding="utf-8") as f_out:
            f_out.write(texte)

        print(f"✅ Terminé : {output_path}")

    except Exception as e:
        print(f"❌ Erreur OCR sur {jpg_name}: {e}")
