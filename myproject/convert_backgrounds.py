import os
import re

# 🛠️ Your actual template folder path
TEMPLATES_DIR = r"C:\Users\ADMIN\Downloads\MGLogistics\myproject\myapp\templates\myapp"

# 🔍 Match background-image or background with url(), ignoring {% static %}
PATTERN = r'url\((["\']?)(?!\{%\s*static)([^"\')]+)(["\']?)\)'

def convert_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(
        PATTERN,
        r"url('{% static '\2' %}')",
        content
    )

    if content != new_content:
        # Backup original
        with open(filepath + ".bak", "w", encoding="utf-8") as backup:
            backup.write(content)

        # Overwrite with updated content
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"✅ Updated: {filepath}")
    else:
        print(f"⚠️ No changes: {filepath}")

def walk_templates():
    for root, _, files in os.walk(TEMPLATES_DIR):
        for file in files:
            if file.endswith(".html"):
                convert_file(os.path.join(root, file))

if __name__ == "__main__":
    print("🌀 Scanning and auto-converting background images...")
    walk_templates()
    print("🎉 Done converting all inline backgrounds to use {% static %}!")
