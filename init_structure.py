from pathlib import Path

folders = [
    "data", "notebooks", "src/etl", "src/features", "src/models", 
    "src/inference", "src/utils", "airflow", "docker", ".github", "docs"
]
files = ["README.md", "requirements.txt", "Makefile", ".gitignore"]

root = Path("./")
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

with open(root / ".gitignore", "w") as f:
    f.write("__pycache__/\n.venv/\ndata/\n*.pkl\n*.log")

for file in files:
    (root / file).touch()

print("📁 Project structure created!")
