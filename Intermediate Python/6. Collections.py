# Collection
# 3-4-22
# Mohammed Shourov

from collections import Counter, deque
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict

print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('-_-_-_-_-_-_-_-Collection: Counter, Namedtuple, OrderedDict, DefaultDict and, Deque-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

# Counter
aCun = 'aaaaaabbbbbcccdddddddddeeeeeeefffffffggggghhhhhhh'
my_Counter = Counter(aCun)
print('My Counter: ', my_Counter)
print('My Counter key: ', my_Counter.keys())
print('My Counter values: ', my_Counter.values())
print('My Most Common Counter: ', my_Counter.most_common())
print('My Most Common item in (Tuples)Counter: ', my_Counter.most_common(1))
print('My Most Common item in (Element & Index)Counter: ', my_Counter.most_common(1)[0])
print('My Most Common item in (Only Element) Counter: ', my_Counter.most_common(1)[0][0])
print('My Only Counter Element: ', list(my_Counter.elements()))

# Namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print('My Namedtuple:  ', pt)
print('My Namedtuple Point:  ', pt.x, pt.y)

# OrderedDict
Ordered_Dict = OrderedDict()
Ordered_Dict['a'] = 1
Ordered_Dict['b'] = 2
Ordered_Dict['c'] = 3
Ordered_Dict['d'] = 4
Ordered_Dict['e'] = 5
print('Ordered Dict: ', Ordered_Dict)

# DefaultDict
d = defaultdict(int) # chnage to float or list
d['a'] = 1
d['b'] = 2
print('Default Dict: ', d)
print('Default Dict w/ key: ', d['a'])
print('Default Dict w/ Fake key: ', d['c'])

# Deque
# Is a duble ended que and it can be used to add & remove from both ends
Deque = deque()
Deque.append(1)
Deque.append(2)
Deque.appendleft(0)
print('My Deque: ', Deque)

Deque.extend([3,4,5,6])
print('Extend The Deque: ',Deque)

Deque.extendleft([-1,-2,-3,-4,-5])
print('Extend The Deque From Left :',Deque)

Deque.clear()
print('Remove From Deque',Deque)

Deque.pop()
print('Remove From Deque',Deque)


print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
