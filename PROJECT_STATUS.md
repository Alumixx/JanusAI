
# 📊 État du projet JanusAI Extraction

## 🔧 Contexte et objectifs

- Objectif : Mettre en place un pipeline d’extraction et d’OCR pour traiter des fichiers `.doc`, `.docx` et `.pdf` afin d’alimenter un projet d’IA spécialisé sur le modèle Janus.
- Environnement : macOS Monterey 12.1 (attention, version non supportée officiellement par Homebrew).
- Environnement Python : Python 3.13 avec environnement virtuel `venv`.

---

## 🏗️ Outils installés

### Paquets Python
- textract → extraction texte DOC/DOCX/PDF
- python-docx → lecture DOCX
- pdfminer.six → PDF texte pur
- pytesseract → OCR d’images
- pdf2image → conversion PDF → images

### Logiciels système
- LibreOffice (`soffice`) → conversion `.doc` en `.txt` ou `.docx`
- antiword → tentative sur `.doc` (deprecated)
- tesseract → OCR
- poppler (`pdftoppm`) → conversion PDF pour OCR (installé via MacPorts)

---

## ⚠️ Problèmes rencontrés

- **Homebrew bloqué** : Incompatibilité avec macOS Monterey pour certains paquets.
- **Solution** : Installation de MacPorts et utilisation de ses paquets pour contourner.
- **Command Line Tools** : Obligé d’utiliser Xcode 13.2 (pas 14.2) compatible Monterey.

---

## 📁 Structure des fichiers

- `docs/` → documents originaux
- `data/texts/` → fichiers `.txt` extraits
- `data/logs_erreurs_extraction.txt` → log erreurs d’extraction
- `data/erreurs.txt` → synthèse des erreurs
- Scripts :
    - `scripts/detect_doc_encoding.py`
    - `scripts/convert_with_soffice.py`
    - `scripts/extract_all_clean.py`
    - `scripts/log_erreurs.py`

---

## 🔒 Recommandations

- **Ne pas faire de mise à jour Homebrew globale**.
- Préférer MacPorts pour installer/mettre à jour les dépendances systèmes.
- Documenter et verrouiller les versions actuelles.
- Vérifier à chaque fois que les outils externes (`soffice`, `tesseract`, `pdftoppm`) sont bien disponibles avant de lancer les scripts.

---

## ✅ Prochaines étapes

1. Vérifier le bon état des installations avec `check_status.py`.
2. Mettre en place un script OCR fallback pour les PDF non extraits.
3. Créer un pipeline global d’extraction.
4. Préparer l’étape hébergement/web (discussion à venir).

