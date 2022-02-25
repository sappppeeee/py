# Lists 2-23-22
# Mohammed Shourov

myList = ['banana', 'cherry', 'apple']
print(myList)

#can be deffernt type of data
myList2 = [5, True, 'apple']
print(myList2)

#index of list (0 - #)
item = myList[0] # first item
item = myList[-1] # last item

# forloop list 
for i in myList:
  print(i)

# if the item is in the list od not 
if 'banana' in myList:
  print('Yes')
else:
  print('no')

# add an item in the list 
myList.append('lemon')
print('Add Item: ',myList)

# add an item in 2nd place on the list
myList.insert(1,'blueberry')
print('Add Item by index: ', myList)

# Remove item
item = myList.pop() # returns the last item or by index and also removes it 
print('Pop Returned Item: ',item) #returned 
print('List without the Item: ',myList) #removed

# Remove item by index
item = myList.remove('cherry') # can cause a ValueError
print('List without the Cherry: ',myList)

# Remove all item
item = myList.clear
print('Remove all item: ',myList)

myList = ['2', '8', '5', '4', '1', '3', '6', '7']
print('Original: ',myList)

# reverse list
myList.reverse()
print('Reversed: ',myList)

# Order the list
# myList.sort()--------------------
#                                  ----- Changes/sorts the list for the entire program.
# print('In Order: ',myList)-------
myNewList = sorted(myList) # newlist become the sorted list
print('In Order: ',myNewList)

# listed in "-", "+", "x", "-/-"
list1 = ['ad'] * 7
print('Multiply List: ',list1)

list2 = [1,2,3,4,5,6,7]
print('Second List: ',list2)

list1And2 = list1 + list2
print('Adding Two list Together: ', list1And2)

# slicing list 
print('   ')
print('Slicing List:=:=: ')
print(' ')

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = numberList[2:6]
print('Slice List (2-6): ', slice)

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = numberList[:6] # Starts from begning ends at 6
print('Starts from 1 ends at 6: ', slice)

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = numberList[6:] # Starts from 6 ends at 10  
print('Starts from 6 ends at 10: ', slice)

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = numberList[::2 ] #Every Second Item
print('Every Second Item: ', slice)

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = numberList[::-1] # Reverse List
print('Reversed List: ', slice)

#Copying List
print(' ')
print('Copying List')
print(' ')

list_org = ['banana', 'cherry', 'apple']

# list_cpy = list(list_org)
list_cpy = list_org.copy() 
# list_cpy = list_org[:]

list_cpy.append('lemon')
print(list_cpy)
print(list_org)

#list comprehension 
numberLists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_comprehension= [i*i for i in numberLists]

print(numberLists)
print(list_comprehension)
