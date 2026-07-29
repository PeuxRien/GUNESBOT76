from pathlib import Path

folders = [
    "src",
    "src/core",
    "src/core/config",
    "src/core/logger",
    "src/core/utils",
    "src/core/events",
    "src/news",
    "src/media",
    "src/video",
    "src/audio",
    "src/agents",
    "src/database",
    "src/plugins",
    "src/seo",
    "src/ui",
    "tests",
    "assets",
    "output",
    "cache",
    "logs",
]

files = [
    "main.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    ".env",

    "src/core/app.py",
    "src/core/banner.py",
    "src/core/config/settings.py",
    "src/core/logger/logger.py",
    "src/core/utils/system.py",
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("ODIN Bootstrap Completed")