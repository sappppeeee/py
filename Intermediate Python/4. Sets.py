# Sets 
# Mohammed Shourov
# 3-3-22

from re import A


print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-__-_Sets: Unordered, Mutable, No Duplicates-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

# Vanilla Sets
mySet ={1,2,3,4,5,6,7,8,9,10}
print('Vanilla Sets: ', mySet)

# Sets w/ string 
mySet = set('Hello World')
print("Sets w/ Unordered String: ", mySet)

#Mutable
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(4)
print("Added Sets: ", mySet)
mySet.remove(4)
print("Remove 4 From Sets: ", mySet) # can cause a key error
mySet.discard(3)
print("Discard 3 From Sets: ", mySet)

# mySet.clear() removes all items
# mySet.pop() removes random item 

# loopping set
mySet ={1,2,3,4,5,6,7,8,9,10}
for x in mySet:
  print("Loopping Set",x) 

# Merging two sets
odds = {1,3,5,7,9}
evens = {0,2,4,6,8,}
primes = {2,3,5,7}

union = odds.union(evens)
print("Merging two sets: ", union)

# intersection evens
intersections = odds.intersection(evens)
print("Intersection evens: ", intersections)

# intersection primes
intersections = odds.intersection(primes)
print("Intersection primes: ", intersections)

# difference between 2 sets
setA ={1,2,3,4,5,6,7,8,9}
setB ={1,2,3,10,11,12}
diff = setB.difference(setA)
print('Difference Between B and A', diff)

setA ={1,2,3,4,5,6,7,8,9}
setB ={1,2,3,10,11,12}
diff = setB.symmetric_difference(setA)
print('Symmetric Difference Between B and A(not the same)', diff)

# Modify Set
setA ={1,2,3,4,5,6,7,8,9}
setB ={1,2,3,10,11,12}
setA.intersection_update(setB)
print("Only prints both set's items: ", setA)

setA ={1,2,3,4,5,6,7,8,9}
setB ={1,2,3,10,11,12}
setA.difference_update(setB)
print("Merging sets A & B: ", setA) 

setA ={1,2,3,4,5,6,7,8,9}
setB ={1,2,3,10,11,12}
setA.update(setB)
print("Merging sets A & B by maching: 4", setA)

# Sub Set
setA ={1,2,3,4,5,6,7,8,9}
setB ={1,2,3}
print("Is setB a sub set of setA: ",setB.issubset(setA))
print("Is seta a sub set of setB: ",setA.issubset(setB))

# Sub Set
print("Is setB a super set of setA: ",setB.issuperset(setA))
print("Is seta a super set of setB: ",setA.issuperset(setB))
# dissjoint true if the set is not in the other set

#copying sets
setA ={1,2,3,4,5,6,7,8,9}
setC = setA
setC.add(10)
print('Both Copies r same',setC)
print('Both Copies r same',setA)

# frozen set
y = frozenset([1,2,3,4,5])
print('A frozen set:  ',y)
# ADD / REMOVE / UPDATE DOSEN'T WORK BUT UNION / INTERSECTION / DIFFERENCE WILL WORK 


print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')