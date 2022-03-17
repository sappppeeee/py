# Exceptions and Errors
# 3-16-22
# Mohammed Shourov

# Syntax Error---------------|
#                            |---------> a - 5 print(a) 
#      Correct Syntax    >   |---------> a - 5
#      Correct Syntax    >   |---------> print(a)


# Exceptions Errors----------|
#    Different Data Type     |---------> a - 5 + '10'


# Module Not Found Errors----|
# also the subclass from-----|
# import errors--------------|
#                            |---------> import ssssssssssss


# Name Errors----------------|
#      Name Not defined   >  |---------> a - 5
#      Name Not defined   >  |---------> b - c


# File Not Found Error
#        Wrong Name     >    |---------> f - open('wrongName-txt')
 

# Value Error----------------| 
#                            |---------> a =[1,2,3,4]
#          Error             |---------> a.remove(5)
#                            |---------> print(a)


# Index Error----------------| 
#                            |---------> a =[1,2,3,4]
#          Error             |---------> a[5] 
#                            |---------> print(a)

# Key Error------------------| 
#                            |---------> my_dict = {'name': 'max'}
#          Error             |---------> my_dict['age]

# Exceptions Errors
#                            |---------> x = -5 
#                            |---------> if x < 0:
#                            |--------->  raise Exception('X should be positive ')

# Assertion Error------------|
#                            |---------> x = -5 
#                            |---------> assert (x>=0), 'X is not Positive'


# Zero Division Error--------|
#                            |---------> a = 5/0


# Exceptions Errors
#                            |---------> try:
#                            |--------->     a = 5/0
#                            |---------> except:
#                            |--------->     print('An Error c )

# Catch Exceptions Errors
print('--Catch Exceptions Errors w/ \"try:" #1')
try:
  a = 5 / 0
except Exception as eX:
  print(eX)

# Catch Errors
print('--Catch Exceptions Errors w/ \"try:" #2')
try:
  a = 5 / 1
  b = a + '10'
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)

# Catch Errors
print('--Catch Exceptions Errors w/ \"try:" #3')
try:
  a = 5 / 0
  b = a + '10'
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)

# Catch Errors
print('--Catch Exceptions Errors w/ \"try:" #4')
try:
  a = 5 / 1
  b = a + 4
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print('Everything Is Fine!!!')

# Catch Errors
print('--Catch Exceptions Errors w/ \"try:" #5')
try:
  a = 5 / 1
  b = a + 4
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print('Everything Is Fine!!!')
finally:
  print('Cleaning Up....')

# Catch Erros with class
class ValueTooHighError(Exception):
  pass

class ValueTooLowError(Exception):
  def __init__(self, message, value):
      self.message = message
      self.value = value

def test_value(x):
  if x > 100:
    raise ValueTooHighError('Value is too high ')
  if x < 5:
    raise ValueTooLowError('Value is too Low', x )

try:
  test_value(200)
except ValueTooHighError as e:
  print(e)
except ValueTooLowError as e:
  print(e.message, e.value)

