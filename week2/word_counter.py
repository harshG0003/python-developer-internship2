
from pathlib import Path

file_name = Path(__file__).parent / "sample.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.split()
    lines = text.splitlines()
    characters = len(text)

    print("\n--- Word Counter ---")
    print("Words:", len(words))
    print("Lines:", len(lines))
    print("Characters:", characters)

except FileNotFoundError:
    print("Error: sample.txt was not found.")
