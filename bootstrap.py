from pathlib import Path

FOLDERS = [
    ".vscode",

    "assets",
    "assets/audio",
    "assets/fonts",
    "assets/logos",
    "assets/music",
    "assets/overlays",
    "assets/stock",

    "cache",

    "config",

    "data",
    "data/news",
    "data/trends",
    "data/channels",
    "data/analytics",

    "database",

    "docs",

    "logs",

    "models",

    "output",
    "output/videos",
    "output/thumbnails",
    "output/subtitles",
    "output/seo",

    "plugins",

    "prompts",

    "src",

    "src/core",
    "src/core/config",
    "src/core/logger",
    "src/core/utils",
    "src/core/events",

    "src/news",
    "src/news/core",
    "src/news/models",
    "src/news/services",
    "src/news/sources",
    "src/news/utils",

    "src/media",
    "src/video",
    "src/audio",
    "src/agents",
    "src/database",
    "src/seo",
    "src/ui",

    "tests",

    "tmp"
]

FILES = [
    "README.md",
    ".gitignore",
    ".env",
    "requirements.txt",
    "main.py",

    "src/core/app.py",
    "src/core/banner.py",

    "src/core/config/settings.py",

    "src/core/logger/logger.py",

    "src/core/utils/system.py",

    "src/news/core/engine.py",
    "src/news/models/news.py",
    "src/news/services/deduplicator.py",
    "src/news/sources/steam.py",
    "src/news/sources/rockstar.py",
]

print()
print("=" * 60)
print("ODIN Bootstrap")
print("=" * 60)
print()

created_folders = 0
created_files = 0

for folder in FOLDERS:
    path = Path(folder)

    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        created_folders += 1
        print(f"[Folder] {folder}")

for file in FILES:
    path = Path(file)

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        created_files += 1
        print(f"[File]   {file}")

print()
print("=" * 60)
print(f"Folders Created : {created_folders}")
print(f"Files Created   : {created_files}")
print("Bootstrap Completed")
print("=" * 60)