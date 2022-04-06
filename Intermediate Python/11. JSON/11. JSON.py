#Json with Python
# 3-25-22
# Mohammed Shourov

import json

# Vanilla Data
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
print("        ")
print("Normal Dictionaries:  ", person)

# convert into JSON:
personJon = json.dumps(person)
print("        ")
print("A Json:               ", personJon)

# use different formatting style
personJonI = json.dumps(person, indent=4, sort_keys=True)
print("        ")
print("A Json w/ indent:  \n \n", personJonI,'\n')

# From Python to JSON (Serialization, Encode)
with open('person.json', 'w') as file:
  json.dump(person, file, indent=4)

# FROM JSON to Python (Deserialization, Decode)
personL = json.loads(personJonI)
print("FROM JSON to Python:  ", personL) 

#  load data from a file and convert it to a Python object
with open('person.json', 'r') as file:
    person = json.load(file)
    print("        ")
    print("FROM JSON to Python:  ",person, '  :w/ \n')