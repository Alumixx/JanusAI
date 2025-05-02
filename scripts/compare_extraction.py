import os
from pdfminer.high_level import extract_text

INPUT_DIR = "docs"
OCR_DIR = "data/texts"
PDFS = [
    "schwarzschild-fev-1916-fr.pdf",
    "schwarzschild-fev-1916-fr (1).pdf",
    "schwarzschild-jan-1916-fr.pdf",
    "schwarzschild-jan-1916-fr (1).pdf"
]

for pdf_name in PDFS:
    input_path = os.path.join(INPUT_DIR, pdf_name)
    ocr_path = os.path.join(OCR_DIR, os.path.splitext(pdf_name)[0] + ".txt")

    print(f"\n=== Comparaison pour {pdf_name} ===")

    # Extraction directe (pdfminer)
    try:
        extracted_text = extract_text(input_path)
        print("🟡 Extraction directe (pdfminer):")
        print(extracted_text[:300].replace("\n", " ") + "...")
    except Exception as e:
        print(f"❌ Erreur extraction directe : {e}")

    # Lecture OCR déjà fait
    try:
        with open(ocr_path, "r", encoding="utf-8") as f:
            ocr_text = f.read()
        print("\n🟢 Texte OCR (pytesseract):")
        print(ocr_text[:300].replace("\n", " ") + "...")
    except Exception as e:
        print(f"❌ Erreur lecture fichier OCR : {e}")
