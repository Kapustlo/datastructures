Currently available data structures:
===================================
  1. Stack
  2. Graph
  3. Tree

Module utils:
=============
from datastructures.utils.utils import *

longest_string(list)
--------------------
Accepts a list of objects that get converted into string and returns the length of the longest one

Example:

``` python
  a = longest_string(["A","BBB","New York"])
  print(a)
  # prints 8
```

Module datastructures:
=====================
Module stack
------------
**from datastructures.stack import Stack**

### Constructor:
Accepts any objects and as much as you want as its constructor parameters

``` python
stack = Stack(1,2,"3",[1,2,3,4])
```

### Fields:
**self.items - Every item stored in the stack**

### Methods:

#### self.get_stack()
Returns a stringified stack visualisation

####  self.get_all_as_list()
Returns a tuple of items stored in the stack

####  self.push(*args)
Pushes as many objects as you passed as parameters

#### self.pop()
Pops the element on top of the stack and returns it

#### self.last()
Returns the item on top of the stack

#### self.size()
Returns the size of the stack

#### self.is_empty()
Returns whether the stack is empty or not

#### self.count(param)
Counts how many items are equal to the one passed as the parameter

// README update coming soon
