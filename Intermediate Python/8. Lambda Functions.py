# Lambda Functions
# 3-16-22
# Mohammed Shourov

from functools import reduce

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_Lambda Functions: \"Lambda argument: expression"_-__-_-_-_--_-_-_-_-_-_-_-_-_')

# Vanilla Lambda Functions
add10 = lambda x: x + 10 # "I'm better than line 15. hehehehe"
print('Vanilla Lambda Functions: ',add10(5))

def add10_func(x):
  return x + 10  # same as line 11

# Lambda Functions multiply
mult = lambda x1,y1: x1*y1
print('Lambda Functions(\"mult(2,7)") multiply: ',mult(2,7)) # Call the function w/ the argument like this:  aFunctionName( w/ agrument "aka input / data / other higher-order function" ) 

# Sort 
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)

print('Vanilla List: ',points2D)
print('Sorted List: ',points2D_sorted)

# Sort w/ Lambda
points2D_sorted_lamda = sorted(points2D, key= lambda x: x[1]) # u can also sort by item index w/ lambda

def sort_by_y(x):
  return x[1]  # same as line 28 but I'm a loser / loner 

print('Sorted Lambda List: ',points2D_sorted_lamda)

# Sorted Lambda List w/ sum of each item
points2D_sorted_lamda_sum = sorted(points2D, key=lambda x: x[0] + x[1])
print('Sorted Lambda List w/ sum of each item: ',points2D_sorted_lamda_sum)

# Map(Function, Sequence)
aL = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bL = map(lambda x: x*2, aL) # Alternative: "bL = [x*2 for x in aL]"
print('Vanilla List: ',aL)
print('Map List w/ Lambda mutly by 2: ',bL) # Use a list as argument or it will print as a map object
print('Map List w/ Lambda mutly by 2: ',list(bL))

# Filter(Function, Sequence)
aF = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bF = filter(lambda x: x%2==0, aF) # Alternative: "bF = [x for x in aF if x%2==0]"
print('Filter List by even w/ Lambda : ',list(bF))

# Reduce(Function, Sequence)
aR = [1, 2, 3, 4]
product_aR = reduce(lambda x,y: x*y, aR) # math: " 1 x 2 = 2, 2 x 3 = 6, 6 x 4 = 24 " end product should be 24
print('Reuce List w/ Lambda : ', product_aR)


print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-') 