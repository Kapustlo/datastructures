Currently available data structures:
  1. Stack
  2. Graph
  3. Tree

Module utils:
  from datastructures.utils.utils import *

  Accepts a list of objects that get converted into string and returns the length of the longest one

  longest_string(list)

  Example:

    a = longest_string(["A","BBB","New York"])
    print(a)

    >> 8

Module datastructures:

  1. Module stack:
      from datastructures.stack import Stack

      Constructor:

        Accepts any objects and as much as you want as its constructor parameters

        stack = Stack(1,2,"3",[1,2,3,4])

      Fields:

        self.items - Every item stored in the stack

      Methods:

        Returns a stringified stack visualisation

        get_stack()

        Returns a tuple of items stored in the stack

        get_all_as_list()

        Pushes as many objects as you passed as parameters

        push(*args)

        Pops the element on top of the stack and returns it

        pop()

        Returns the item on top of the stack

        last()

        Returns the size of the stack

        size()

        Returns whether the stack is empty or not

        is_empty()

        Counts how many items are equal to the one passed as the parameter

        count(param)
        
// Update of README will come out soon
