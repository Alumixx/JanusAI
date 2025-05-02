import os

DOCS_DIR = "docs"
TEXTS_DIR = "data/texts"
ERREURS_FILE = "data/erreurs.txt"

# Charger les noms de fichiers d'erreurs pour référence
if os.path.exists(ERREURS_FILE):
    with open(ERREURS_FILE, "r", encoding="utf-8") as f:
        erreurs = [ligne.split(" — ")[0].strip() for ligne in f.readlines()]
else:
    erreurs = []

print("🔍 Audit final des extractions :\n")

for filename in os.listdir(DOCS_DIR):
    base, ext = os.path.splitext(filename)
    txt_file = os.path.join(TEXTS_DIR, base + ".txt")

    if filename in erreurs:
        print(f"⚠️  {filename} est listé comme erreur → OK (trace conservée)")
    elif os.path.exists(txt_file):
        print(f"✅ {filename} → extrait présent")
    else:
        print(f"❌ {filename} → PAS trouvé dans data/texts/ (non listé dans erreurs.txt)")
