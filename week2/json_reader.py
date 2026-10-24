
import json
from pathlib import Path

file_name = Path(__file__).parent / "students.json"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("\n--- Student Records ---")

    for student in data["students"]:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Marks:", student["marks"])
        print("----------------------")

except FileNotFoundError:
    print("Error: students.json was not found.")

except json.JSONDecodeError:
    print("Error: The JSON file contains invalid data.")

except KeyError:
    print("Error: A required student field is missing.")
