import os
import textract
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

# === CONFIGURATION ===
INPUT_DIR = "docs"
OUTPUT_DIR = "data/texts"
LOG_PATH = "data/logs_erreurs_extraction.txt"
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".doc"]

# Crée les dossiers nécessaires
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Vide le fichier de log à chaque exécution
open(LOG_PATH, "w").close()

# === FONCTIONS ===

def extract_docx(file_path):
    """Extrait le texte d’un fichier DOCX"""
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

# === TRAITEMENT ===
fichiers_extraits = 0
fichiers_ignores = 0
fichiers_total = 0

for root, _, files in os.walk(INPUT_DIR):
    print(f"🔍 Dossier exploré : {root}, fichiers trouvés : {len(files)}")
    for filename in files:
        ext = os.path.splitext(filename)[1].lower()
        if ext not in SUPPORTED_EXTENSIONS:
            continue

        fichiers_total += 1
        file_path = os.path.join(root, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(OUTPUT_DIR, base_name + ".txt")

        if os.path.exists(output_path):
            print(f"⏭️  Déjà extrait, on ignore : {filename}")
            fichiers_ignores += 1
            continue

        print(f"📄 Extraction de : {filename}")
        try:
            if ext == ".pdf":
                text = extract_pdf_text(file_path)
            elif ext == ".docx":
                text = extract_docx(file_path)
            elif ext == ".doc":
                text = textract.process(file_path).decode("utf-8")
            else:
                text = "[Format non supporté]"

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            fichiers_extraits += 1

        except Exception as e:
            print(f"  ❌ Erreur sur {filename}: {e}")
            with open(LOG_PATH, "a", encoding="utf-8") as log_file:
                log_file.write(f"❌ Erreur sur {filename}: {e}\n")

# === RAPPORT FINAL ===
print("\n📊 Bilan :")
print(f"   Total de fichiers détectés : {fichiers_total}")
print(f"   ✅ Fichiers extraits       : {fichiers_extraits}")
print(f"   ⏭️  Fichiers ignorés       : {fichiers_ignores}")
print(f"   📁 Log erreurs             : {LOG_PATH}")
print("🎉 Extraction terminée.")
