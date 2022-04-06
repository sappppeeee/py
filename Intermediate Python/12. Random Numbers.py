# Random Numbers 
# Mohammed Shourov
# 3-29-22

import random
import string
import secrets
import numpy as np

# random float in [0,1)
a = random.random() 
print(a)

# random float in range [a,b]
a = random.uniform(1,10)  
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1,10)  
print(a)

# random integer in range [a,b). b is excluded
a = random.randrange(1,10)  
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0,1)  
print(a)

# choose a random element from a sequence
mylist =  string.ascii_uppercase
a = random.choice(mylist)
print(a)

# choose k unique random elements from a sequence / no repeat
a = random.sample(mylist, 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(mylist, k=3)
print(a)

# shuffle list in place
mylist1 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
random.shuffle(mylist1)
print(mylist)

# Generate same random number multiple time
random.seed(1)
print('Seed 1#: ',random.random())
print('Seed 1#: ',random.randint(1,10))
random.seed(2)
print('Seed 2#: ',random.random())
print('Seed 2#: ',random.randint(1,10))
random.seed(1)
print('Seed 1#: ',random.random())
print('Seed 1#: ',random.randint(1,10))
random.seed(2)
print('Seed 2#: ',random.random())
print('Seed 2#: ',random.randint(1,10))

# The secrets module / random integer in range [0, n).
b = secrets.randbelow(10)
print('secrets.randbelow: ', b)

# return an integer with k random bits.
b = secrets.randbits(4)
print('secrets.randbelow: ', b)

# choose a random element from a sequence
b = secrets.choice(mylist)
print('secrets.choice(mylist): ', b) 

# numpy

# generate nd array with random floats, arrays has size (d0,d1,…,dn)
c = np.random.rand(3,3)
print('Generate Array: \n',c)

# generate nd array with random integers in range [a,b) with size n
c = np.random.randint(0,10,(3,4))
print('Generate Array: \n',c)

# Randomly Shuffle a nd array.
# Only Shuffles the array along the first axis of a multi-dimensional array
carr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(' Array: ',carr)
np.random.shuffle(carr)
print('Shuffle Array: ',carr)

# Generate w/ seed Array
np.random.seed(1)
s = np.random.randint(1,10,(3,3))
print('Generate w/ seed 1# Array: \n',s)

np.random.seed(2)
s = np.random.rand(3,3)
print('Generate w/ seed 2# Array: \n',s)

np.random.seed(1)
s = np.random.randint(1,10,(3,3))
print('Generate w/ seed 1# Array: \n',s)

np.random.seed(2)
s = np.random.rand(3,3)
print('Generate w/ seed 2# Array: \n',s)
