#!/usr/bin/env python3
import sys
import os
import json

def init_project():
    # Creates default files if they don't exist
    if not os.path.exists('slides.md'):
        with open('slides.md', 'w') as f:
            f.write("# Viewfoil Sample Presentation\n\n---\n\n## Second Slide\n")
        print("Created slides.md")
    else:
        print("slides.md already exists. Skipping.")

    if not os.path.exists('config.json'):
        with open('config.json', 'w') as f:
            json.dump({
                "theme": "default",
                "slides_delimiter": "---"
            }, f, indent=2)
        print("Created config.json")
    else:
        print("config.json already exists. Skipping.")

def convert_to_notebook():
    # Load config.json
    if not os.path.exists('config.json'):
        print("Error: config.json not found. Run './manage.py init' to create it.")
        return

    with open('config.json', 'r') as f:
        config = json.load(f)

    delimiter = config.get("slides_delimiter", "---")
    print(f"Using slide delimiter: {delimiter}")

    # Placeholder for slide conversion
    print("Converting slides.md to .ipynb (not implemented yet)")

def main():
    if len(sys.argv) < 2:
        print("Usage: manage.py [init|convert]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "init":
        init_project()
    elif command == "convert":
        convert_to_notebook()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
