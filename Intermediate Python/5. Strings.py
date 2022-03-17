# String
# 3-4-22
# Mohammed Shourov

from timeit import default_timer as timer

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-Strings: Ordered, immutable, texr representation_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

# Vanilla Strings
my_string = "Vanilla Strings: Hello World"
print(my_string) 

# An apostrophe in string
apostrophe = 'An apostrophe \'s \'ing '
print(apostrophe) 

# multi-Line string
multiLine = """ A multi-Line 
string """

# A multi-Line string to single line
multiLineSingle = """ A multi-Line \
string to single line"""
print(multiLineSingle)

# index of string
my_indexS = my_string[1]
print(my_indexS,"index #1")
# my_string[1] = 'h'     ---> Cause String objest dose not support item assigment

# slicing string
slicingString = my_string[0:7]
print('Slicing String with SubString: ', slicingString)

slicingString = my_string[::]
print('Slicing String with SubString w/ all: ', slicingString)

slicingString = my_string[::2]
print('Slicing String with SubString w/ 2: ', slicingString)

slicingString = my_string[::-1]
print('Slicing String with SubString reversed: ', slicingString)

# concatenate strings 
stringA = "Hello"
stringB = "MO Shourov"
stringAnB = stringA + " " + stringB
print('concatenate strings: ', stringAnB)

# looping string
for i in my_string:
  print('Looping string:',i) 

# check 4 item
if 'world' in my_string:
  print("check 4 item: yes")
else:
  print('check 4 item: No')

# Remove space
myString = '      Hello World         '
print('String w/ space: ', myString)
myStringW = myString.strip()
print('String w/out space: ', myStringW)

# upperCase / LowerCase / Starts With / Find index / count String / replce
myString = 'Hello World' 
print('upperCase: ',myString.upper())
print('LowerCase: ',myString.lower())
print('If string starts w/ Hello: ',myString.startswith('Hello'))
print('Find Index \"o": ',myString.find('o'))
print('Count l in String: ',myString.count('l'))
print('Replace World w/ Universe: ',myString.replace('World','Universe'))

# String to list 
my_list = myString.split()
print('String to list: ',my_list)
newString = ''.join(my_list)
print('list to string: ',newString)

# .joint IMPORTANT
myList = ['a'] * 20
print('A list: ',myList)

# Bad python
starT = timer()
ajointString = ''
for i in myList:
  ajointString +=i
print('Bad Joint list from string: ',ajointString)
stopT = timer()
print('Bad python: ', stopT-starT)

# Smarter Way
starTS = timer()
jointString = ''.join(myList)
print('Joint list from string: ',jointString)
stopTS = timer()
print('Smarter Way: ', stopTS-starTS)

# fromating ---> % / .formart() / f-string
varA = 'Tom'
my_yS = 'the variable is %s' % varA
print('fromating ---> %: ',my_yS)

# Integer 
varA = 5
my_yS = 'the variable is %d' % varA
print('fromating ---> %: ',my_yS) 

# Float
varA = 5.3221144123
my_yS = 'the variable is %.10f' % varA
print('fromating ---> %: ',my_yS) 

# .format()
varY = 2.431124325
my_yS = 'the variable is {:.2f} and {}'.format(varA, varY)
print('fromating ---> .format(): ',my_yS)

# New Farmating
my_yS = f'the variable is {varA} and {varY}'
print('fromating ---> New Farmating: ',my_yS)


print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')