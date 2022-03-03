# Dictionaries 
# Mohammed Shourov
# 3-2-22

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('-_-_-_-_-_-_-_-_-_Dictionaries: Unordered, mutable, key : value pairs_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

# Vanilla Dictionarie
myDict = {"name": "Max", 'age': 28, "city": "New York"}
print('Vanilla Dictionarie: ', myDict)

# Dictionarie with Dictionarie function
myDictF = dict(name='Marry', age=27, City='Boston')
print('Dictionarie with Dictionarie function: ', myDictF)

# CAN CAUSE A KEY ERROR

# Adding Item
myDict['email'] = 'max@xyz.com'
print('New Item Dictionarie: ', myDict)

# Replace Item
myDict['email'] = 'coolMax@xyz.com'
print('Replace Item Dictionarie: ', myDict)

# Delete Item
del myDict['name']
print('Delete Item Method 1 : ', myDict)

myDict.pop('age')
print('Delete Item Method 2 : ', myDict)

myDict.popitem()
print('Delete Item Method 3 : ', myDict)

myDict = {"name": "Max", 'age': 28, "city": "New York"}
# find item in Dictionarie
if 'name' in myDict:
  print("Is name is in the Dictionarie: ",myDict['name'])

try:
  print(myDict['lastName'])
except:
  print("Is Last Name is in the Dictionarie: ",'!!!Error!!!!')

# looping through Dictionarie
for key in myDict:
  print("Looping Through Dictionarie: ",key)

for key in myDict.keys():
  print("Looping Through Dictionarie: ",key)

for value in myDict.values():
  print("Looping Through Dictionarie by value: ", value) 

for key, value in myDict.items():
  print("Looping Through Dictionarie by value & Key: ", key," : ", value)

# Copy Dictionarie
myDictCopy = myDict
print("Copy Dictionarie: ", myDictCopy)

myDictCopy['email'] = 'max@xyz.com'
print("Copy Dictionarie myDictCopy: ", myDictCopy)
print("Copy Dictionarie myDict: ", myDict)
print("!!!!Now both Dictionaries point to the same place(email) in the Dictionaries!!!!")

myDictCopy = myDict.copy()
print("Actual Copy  Dictionarie: ", myDictCopy)

myDictCopy = dict(myDict)
print("Actual Copy Dictionarie w/ dict() function: ", myDictCopy)

# Merging two Dictionarie
myDict = {"name": "Max", 'age': 28, "city": "New York"}
myDictF = dict(name='Marry', age=27, City='Boston')
myDict.update(myDictF)
print('Merging two Dictionarie: ', myDict)

myDictN = {3:9, 6:36, 9:81}
print(myDictN)

value = myDictN[3]
print('Value by key not index Dictionarie: ', value)

mytuple = (8,7)
myDictT = {mytuple: 15}
print('Dictionarie w/ tuple: ', myDictT)
print('Dictionarie run w/ list it will cause a tyoe error!!!!!')

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')