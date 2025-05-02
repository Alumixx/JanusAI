import os
import pytesseract
from pdf2image import convert_from_path

# === CONFIGURATION ===
ERREURS_FILE = "data/erreurs.txt"
INPUT_DIR = "docs"
OUTPUT_DIR = "data/texts"
LANG = "fra"  # ou "eng" si ton texte est en anglais

# Vérifie les dépendances
assert os.path.exists(ERREURS_FILE), "Fichier d'erreurs manquant"

# Récupère les fichiers PDF à retraiter
with open(ERREURS_FILE, "r", encoding="utf-8") as f:
    lignes = f.readlines()

pdfs_a_traiter = [
    ligne.split(" — ")[0] for ligne in lignes
    if ligne.strip().endswith(".pdf")
]

if not pdfs_a_traiter:
    print("✅ Aucun PDF à retraiter avec OCR.")
    exit()

# OCR sur chaque PDF
for pdf_name in pdfs_a_traiter:
    input_path = os.path.join(INPUT_DIR, pdf_name)
    base_name = os.path.splitext(pdf_name)[0]
    output_path = os.path.join(OUTPUT_DIR, base_name + ".txt")

    try:
        print(f"📄 OCR en cours : {pdf_name}")
        images = convert_from_path(input_path)
        texte_total = ""

        for i, image in enumerate(images):
            texte = pytesseract.image_to_string(image, lang=LANG)
            texte_total += f"\n\n--- Page {i+1} ---\n\n{texte}"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(texte_total)

        print(f"✅ Terminé : {output_path}")

    except Exception as e:
        print(f"❌ Erreur OCR sur {pdf_name}: {e}")
