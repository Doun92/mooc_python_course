# Write your solution here
import json

def print_persons(filename: str):
    with open(filename, "r") as json_file:
        data = json_file.read()
        persons = json.loads(data)

        for person in persons:
            hobbies = ""
            for hobby in person['hobbies']:
                hobbies += hobby + ", "
            print(f"{person['name']} {person['age']} years ({hobbies[:-2]})")

if __name__ == "__main__":
    print_persons("src\\file1.json")