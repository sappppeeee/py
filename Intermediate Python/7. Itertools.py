# Itertools
# 3-11-22
# Mohammed Shourov

from multiprocessing.sharedctypes import Value
import operator
from itertools import product
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate
from itertools import groupby
from itertools import count, cycle ,repeat

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-Itertools: product, permutations, combination, accumulate, group-by, and infinite iterators_-_-_')

# Product
productA = [1,3]
productB = [3,4]

prod = product(productA,productB)
print('Product: ',list(prod))

prod = product(productA,productB, repeat=2 )
print('Product by 2: ',list(prod))

# Permutations
permutationsA = [1,2,3]
perm = permutations(permutationsA)
print('Permutation: ',list(perm))

perm = permutations(permutationsA, 2)
print('Permutation w/ length of 2: ',list(perm))

# Combination
combinationA = [1,2,3,4]
comb = combinations(combinationA, 2)
print('Combination w/ length of 2: ',list(comb))
combReplace = combinations_with_replacement(combinationA, 2)
print('Combination With Replacement: ',list(combReplace))

# Accumulate
AccumulateA = [1,2,3,4]
print('Before Accumulate: ',AccumulateA)

Acc= accumulate(AccumulateA)
print('After Accumulate: ',list(Acc))

Accm= accumulate(AccumulateA, func=operator.mul)
print('Accumulate Multply: ',list(Accm))

AccumulateMax = [1,2,5,3,4]
print('Before Accumulate Max: ',AccumulateMax)

Accmax= accumulate(AccumulateMax, func=max)
print('After Accumulate  Max: ',list(Accmax))

# group-by
def smaller_than_3(x):
  return x < 3

groupbyA =[1,2,3,4]
group_obj = groupby(groupbyA, key=smaller_than_3) # can also do this: key=lambda x: x<3
print('Group By Object: ',groupbyA)

for key, value in group_obj:
  print(key, list(value))

# group-by person
persons = [{'name': 'Tim', 'age': 25},{'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27},{'name': 'Claire', 'age': 28}]

group_objP = groupby(persons, key=lambda x: x['age'])
for  key, value in group_objP:
  print(key, list(value))

# infinite iterators
# count
for i in count(10):
  print('This will create a loop that starts at 10 & ends at 15 / can run for infinite w/out a breaker:  ',i)
  if i == 15:
    break

# cycle
cyA =[1,2,3,4]
for i in cycle(cyA):
  print('This will create a loop that cycle through \"cyA" list / can run for infinite w/out a breaker:  ',i)
  if i == 4:
    break

# repeat
repA =[1,2,3,4]
for i in repeat(repA,5):
  print('This will create a loop that cycle through \"cyA" list / can run for infinite w/out a breaker:  ',i)

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')