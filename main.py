"""Task 1"""
"""name = "Hello file world!"
with open('myfile.txt', 'w') as file_object:
    file_object.write(name)

with open('myfile.txt') as file_object:
    name = file_object.read()
print(name)"""
import json
import func

phonebook = loaddata()
with open("phonebook.txt", "w") as pb:
    rec = {
        'first_name': input("first name: "),
        'last_name': input("last name:  "),
        'tel_number': input("telephone number: "),
        'city': input("city: ")
    }

    pb.write(json.dumps(rec) + "\n")
