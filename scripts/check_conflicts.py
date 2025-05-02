import os

# Liste simple de modules standards et populaires (ajoute-en si besoin)
known_modules = [
    'os', 'sys', 're', 'json', 'subprocess', 'shutil', 'math', 'random',
    'datetime', 'time', 'pytesseract', 'pdf2image', 'textract', 'docx',
    'numpy', 'pandas', 'matplotlib', 'seaborn', 'scipy', 'sklearn'
]

scripts_dir = 'scripts'
conflicts = []

if not os.path.exists(scripts_dir):
    print(f"❌ Dossier '{scripts_dir}' introuvable")
else:
    for filename in os.listdir(scripts_dir):
        if filename.endswith('.py'):
            base = os.path.splitext(filename)[0]
            if base in known_modules:
                conflicts.append(filename)

if conflicts:
    print("⚠️  Fichiers qui peuvent entrer en conflit avec des modules Python :")
    for f in conflicts:
        print(f"   → {f}")
else:
    print("✅ Aucun conflit de nom détecté dans le dossier 'scripts/'")
