# Python has a great built-in list type named "list".
# List literals are written within square brackets [ ].
# Lists work similarly to strings -- use the len() function
# and square brackets [ ] to access data, with the first element at index 0.

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting a position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())

# Using Lists as Stacks
# The list methods make it very easy to use a list as a stack,
# where the last element added is the first element retrieved
# (“last-in, first-out”). To add an item to the top of the stack,
#  use append().
#  To retrieve an item from the top of the stack, use pop()
# without an explicit index.

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

# Using Lists as Queues
# It is also possible to use a list as a queue, where the first element
# added is the first element retrieved (“first-in, first-out”);
# however, lists are not efficient for this purpose. While appends and pops
# from the end of list are fast, doing inserts or pops from the beginning
# of a list is slow (because all of the other elements have to be
# shifted by one).

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
print(queue.popleft())  # The first to arrive now leaves
print(queue.popleft())  # The second to arrive now leaves
print(queue)  # Remaining queue in order of arrival

# List Comprehensions
# List comprehensions provide a concise way to create lists.
# Common applications are to make new lists where each element
# is the result of some operations applied to each member of another sequence
# or iterable, or to create a subsequence of those elements that satisfy
# a certain condition.

# For example, assume we want to create a list of squares, like:
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

# this listcomp combines the elements of two lists if they are not equal:
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)

# A tuple is a sequence of immutable Python objects.
# Tuples are sequences, just like lists. The differences between
# tuples and lists are, the tuples cannot be changed unlike lists
# and tuples use parentheses, whereas lists use square brackets.

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x * 2 for x in vec])
# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# apply a function to all the elements
print([abs(x) for x in vec])
# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([fruit.strip() for fruit in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(6)])
# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# List comprehensions can contain complex expressions and nested functions:
from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# The following list comprehension will transpose rows and columns:
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# In the real world, you should prefer built-in functions
# to complex flow statements. The zip() function would do a great job
# for this use case:
print(list(zip(*matrix)))

# The del statement
# The del statement can also be used to remove slices from
# a list or clear the entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)

# Tuples and Sequences
# We saw that lists and strings have many common properties,
# such as indexing and slicing operations. They are two examples
# of sequence data types
# There is also another standard sequence data type: the tuple.
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable:
# t[0] = 88888 # error

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

# Empty tuples are constructed by an empty pair of parentheses;
# a tuple with one item is constructed by following a value with a comma
empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)

# Sets
# Python also includes a data type for sets. A set is an unordered collection
# with no duplicate elements. Basic uses include membership testing and
# eliminating duplicate entries. Set objects also support mathematical operations
# like union, intersection, difference, and symmetric difference.

# Note: to create an empty set you have to use set(), not {};
# the latter creates an empty dictionary

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed
print('orange' in basket)  # fast membership testing
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a) # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# Dictionaries
# Unlike sequences, which are indexed by a range of numbers,
# dictionaries are indexed by keys, which can be any immutable type;
# strings and numbers can always be keys.
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)

# The dict() constructor builds dictionaries directly
# from sequences of key-value pairs:
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# dict comprehensions can be used to create dictionaries
# from arbitrary key and value expressions:
print({x: x**2 for x in (2, 4, 6)})

print(dict(sape=4139, guido=4127, jack=4098))

# Looping Techniques
# When looping through dictionaries, the key and corresponding value can be
# retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value
# can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time,
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse, first specify the sequence in
# a forward direction and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order, use the sorted() function which
# returns a new sorted list while leaving the source unaltered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# It is sometimes tempting to change a list while you are looping over it; however,
# it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)











