import os
import re

# === Chemins ===
INPUT_DIR = "docs"
OUTPUT_DIR = "data/texts"
EXTRACTION_LOG = "data/logs_erreurs_extraction.txt"
ERROR_OUTPUT = "data/erreurs.txt"

# Récupère les fichiers originaux (sans extension)
docs_files = {
    os.path.splitext(f)[0]: f for f in os.listdir(INPUT_DIR)
    if os.path.isfile(os.path.join(INPUT_DIR, f))
}

# Récupère les fichiers extraits (.txt uniquement)
extracted_files = {
    os.path.splitext(f)[0] for f in os.listdir(OUTPUT_DIR)
    if f.endswith(".txt")
}

# Fichiers non extraits
non_extracted = sorted(set(docs_files.keys()) - extracted_files)

# Parse le fichier de log pour erreurs explicites
errors_details = {}
if os.path.exists(EXTRACTION_LOG):
    with open(EXTRACTION_LOG, "r", encoding="utf-8") as log_file:
        for line in log_file:
            match = re.match(r"❌ Erreur sur (.*?): (.*)", line)
            if match:
                filename, message = match.groups()
                base_name = os.path.splitext(filename)[0]
                errors_details[base_name] = message

# Création du fichier d’erreurs consolidé
with open(ERROR_OUTPUT, "w", encoding="utf-8") as out:
    for base_name in non_extracted:
        original_file = docs_files[base_name]
        error_msg = errors_details.get(base_name, "Non extrait (raison inconnue)")
        out.write(f"{original_file} — {error_msg}\n")

print(f"✅ Fichier d’erreurs généré : {ERROR_OUTPUT} ({len(non_extracted)} fichiers)")

