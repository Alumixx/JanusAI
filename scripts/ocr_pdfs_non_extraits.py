import os
import pytesseract
from pdf2image import convert_from_path

# === CONFIGURATION ===
PDFS = [
    "schwarzschild-fev-1916-fr.pdf",
    "schwarzschild-fev-1916-fr (1).pdf",
    "schwarzschild-jan-1916-fr.pdf",
    "schwarzschild-jan-1916-fr (1).pdf"
]
INPUT_DIR = "docs"
OUTPUT_DIR = "data/texts"
LANG = "fra"  # Utilise "eng" si le texte est en anglais

# OCR sur chaque PDF
for pdf_name in PDFS:
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
