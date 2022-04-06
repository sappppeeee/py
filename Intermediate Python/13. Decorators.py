# Decorators
# Mohammed Shourov
# 3-31-22

import functools
from timeit import repeat 

# Function decorators
print('------------------------------------------------------')
print('# Function decorators')
print('------------------------------------------------------')

def my_decorator(func):
  def wrapper():
    print('start')
    func()
    print('end ')
  return wrapper

@my_decorator 
def my_function():
    print('Alex')
# "my_function = my_decorator(my_function)" we can use this method but line 12 is better
my_function()

# Function decorators example 2
print('------------------------------------------------------')
print('# Function decorators example 2')
print('------------------------------------------------------')

def my_decorator(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print('start')
    result = func(*args, **kwargs)
    print('end')
    return result
  return wrapper

@my_decorator 
def add5(x):
  return x + 5
# "my_function = my_decorator(my_function)" we can use this method but line 12 is better
result = add5(10)
print(result)
print(help(add5))
print(add5.__name__)

# The final template for own decorators

#          Code Start

# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do something before
#         result = func(*args, **kwargs)
#         # Do something after
#         return result
#     return wrapper

#           End Code

print('------------------------------------------------------')
print('# Function decorators example 3')
print('------------------------------------------------------')

def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times=10)
def greet(name): 
  print(f'Hello {name}')

greet('Alex')