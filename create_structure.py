from pathlib import Path

# Project folder structure
folders = [
    "app",
    "app/templates",
    "app/static/css",
    "app/static/js",
    "worker",
    "infra",
    "scripts",
    "docs",
]

# Project files
files = [
    # Root files
    "requirements.txt",
    ".env",
    ".env.example",
    ".gitignore",
    "README.md",
    
    # Backend files
    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/db.py",
    "app/aws.py",
    "app/vector.py",
    "app/rag.py",
    "app/memory.py",
    "app/gaurdrail.py",
    "app/graph.py",
    "app/observability.py",
    
    # Frontend files
    "app/templates/index.html",
    "app/static/css/styles.css",
    "app/static/js/app.js",
    
    # Document injestion files
    "worker/__init__.py",
    "worker/ingest.py",
    
    # Database and infrastructure files
    "infra/schema.sql",
    "scripts/init_db.py",
    
    # Documentation files
    "docs/setup.md",
]

def create_structure():
    project_root = Path(__file__).resolve().parent

    # Create folders
    for folder in folders:
        (project_root / folder).mkdir(parents=True, exist_ok=True)
    
    # Create files
    for file in files:
        path = project_root / file
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
        
    print("Project structure created successfully.")
    print(f"Folders created: {len(folders)}")
    print(f"Files created: {len(files)}")
    
if __name__ == "__main__":
    create_structure()


    
    