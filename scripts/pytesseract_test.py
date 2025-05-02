import pytesseract
from pdf2image import convert_from_path
import os

pdf_path = "docs/schwarzschild-fev-1916-fr.pdf"  # exemple
output_txt = "data/texts/schwarzschild-fev-1916-fr.txt"

# Convertit chaque page PDF en image
images = convert_from_path(pdf_path)

# Applique l’OCR à chaque image
full_text = ""
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang="fra")  # ou "eng" selon la langue
    full_text += f"\n\n--- Page {i+1} ---\n\n{text}"

# Sauvegarde le texte
with open(output_txt, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"✅ OCR terminé : {output_txt}")
