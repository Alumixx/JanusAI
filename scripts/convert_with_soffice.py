import os
import subprocess

# === Chemins ===
INPUT_DIR = "docs"
OUTPUT_DIR = "data/texts"

# Assure-toi que le dossier de sortie existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Cherche les fichiers .doc non extraits
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(".doc"):
        base_name = os.path.splitext(filename)[0]
        txt_path = os.path.join(OUTPUT_DIR, base_name + ".txt")
        doc_path = os.path.join(INPUT_DIR, filename)

        if os.path.exists(txt_path):
            print(f"✅ Déjà extrait : {filename}")
            continue

        print(f"🔄 Tentative de conversion via LibreOffice : {filename}")
        try:
            # Appel à LibreOffice en mode headless pour convertir en txt
            subprocess.run([
                "soffice",
                "--headless",
                "--convert-to", "txt:Text",
                "--outdir", OUTPUT_DIR,
                doc_path
            ], check=True)

            print(f"✅ Conversion réussie : {filename}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Échec conversion {filename} : {e}")
