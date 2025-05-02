import os
import shutil

# Vérification des commandes système
tools = ['soffice', 'tesseract', 'pdftoppm']
print("🔍 Vérification des outils système :")
for tool in tools:
    path = shutil.which(tool)
    if path:
        print(f"✅ {tool} trouvé : {path}")
    else:
        print(f"❌ {tool} NON trouvé dans le PATH")

# Vérification des paquets Python
def check_python_package(package_name, import_name=None):
    try:
        if import_name is None:
            import_name = package_name
        mod = __import__(import_name)
        version = getattr(mod, "__version__", "version inconnue")
        print(f"✅ {package_name} installé, version {version}")
    except ImportError:
        print(f"❌ {package_name} NON installé")

print("\n🔍 Vérification des paquets Python :")
check_python_package("pytesseract")
check_python_package("pdf2image")
check_python_package("textract")
check_python_package("python-docx", "docx")

# Vérification des fichiers extraits
DOCS_DIR = "docs"
TEXTS_DIR = "data/texts"
if not os.path.exists(DOCS_DIR):
    print(f"\n❌ Dossier {DOCS_DIR} non trouvé")
else:
    print(f"\n📂 Vérification des fichiers dans {DOCS_DIR} :")
    for f in os.listdir(DOCS_DIR):
        base, ext = os.path.splitext(f)
        txt_file = os.path.join(TEXTS_DIR, base + ".txt")
        if os.path.exists(txt_file):
            print(f"✅ {f} → extrait")
        else:
            print(f"❌ {f} → NON extrait")
