# Tuples 
# 2-24-22
# Mohammed Shourov

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_Tuples: ordered, immutable, allows duplicates elments_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')


# A Tuple
mytuple = ('max', 28, 'boston')
print('A Tuple:  ', mytuple)

# Not a Tuple
Notatuple = ('max')
print('Not a Tuple:  ', Notatuple)

# Is a Tuple
Isatuple = ('max', )
print('Is a Tuple:  ', Isatuple)

# Built In Tuple
myList = ['banana', 'cherry', 'apple']
builtInTuple = tuple(myList)
print('Built In Tuple:  ', builtInTuple)

# Tuple Index
itemT = builtInTuple[0]
print('Tuple Index 1:  ', itemT)

# Change Tuple 
#mytuple[0] = 'Tim'  'WILL CAUSE A TYPE - ERROR"

# Iterate Tuples
for i in mytuple:
  print(i)

# Is Element Is Inside The Tuple
if 'max' in mytuple:
  print("Yes")
else:
  print('NO')

# Others
mytuple2 = ('a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','g')
print('The length of the Tuple:  ',len(mytuple2))
print('Count the letter G:  ', mytuple2.count('g'))
print('The length of the Tuple:  ',len(mytuple2))
print('Index of P in Tuple:  ', mytuple2.index('p'))

# Tuple to List
myListT = list(mytuple2)
print('Tuple to List:  ', myListT)

# Tuple to List
mytupleL = tuple(myListT)
print('List To Tuple:  ', mytupleL)

# slicing with Tuple
numT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
Tnum = numT[2:10]
print('Tuple From index #2 - #5:  ', Tnum)

numT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
Tnum = numT[2:]
print('Tuple From index #2 - end:  ', Tnum)

numT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
Tnum = numT[::-1]
print('Tuple From index reversed:  ', Tnum)

numT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
Tnum = numT[::2]
print('Tuple From index counting by 2:  ', Tnum)

# unpacking
my_tuple = ('max', 28, 'boston')
name, age, city =  my_tuple # CAN CAUSE A VALUE ERROR
print('Unpacking Tuple:  ',name, age, city )

numT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

I1, *I2, I11 = numT
print(I1)
print(I2)
print(I11)

# List Vs Tuple
print('List Vs Tuple')
from ast import stmt
import sys
numT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
numL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('List has: ', sys.getsizeof(numL), 'Bytes')
print('Tuple has: ', sys.getsizeof(numT), 'Bytes')

import timeit
print('List has: ', timeit.timeit(stmt='[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]', number= 1000000,),'Sec')
print('Tuple has: ', timeit.timeit(stmt='(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)', number= 1000000,),'Sec')

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')