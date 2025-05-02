import os

DOCS_DIR = "docs"
REPORT_PATH = "data/rapport_formats_doc.txt"
os.makedirs("data", exist_ok=True)


def detect_file_type(file_path):
    try:
        with open(file_path, "rb") as f:
            header = f.read(1024)

        if header.startswith(b'{\\rtf'):  # Signature RTF
            return "RTF"
        elif header.startswith(b'\xd0\xcf\x11\xe0'):  # OLE signature
            return "Word binaire (.doc)"
        elif b'\0' not in header:
            return "Texte brut ou inconnu"
        else:
            return "Autre format binaire"
    except Exception as e:
        return f"Erreur de lecture: {e}"


with open(REPORT_PATH, "w", encoding="utf-8") as report:
    for filename in os.listdir(DOCS_DIR):
        if filename.lower().endswith(".doc"):
            file_path = os.path.join(DOCS_DIR, filename)
            type_result = detect_file_type(file_path)
            report.write(f"{filename} — {type_result}\n")

print(f"✅ Rapport généré : {REPORT_PATH}")
