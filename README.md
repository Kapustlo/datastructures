Currently available data structures:
===================================
  1. Stack
  2. Graph
  3. Tree

Module utils:
=============
``` python
from datastructures.utils.utils import *
```

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
Module Stack
------------
``` python
from datastructures.stack import Stack
```

### Constructor:
Accepts any objects and as much as you want as its constructor parameters

``` python
stack = Stack(1,2,"3",[1,2,3,4])
```

### Fields:
 ``` python
 stack.items #All objects stored in the stack (list)
 ```

### Methods:

``` python
stack.get_stack() #Returns a stringified stack visualisation

stack.get_all_as_list() #Returns a tuple of items stored in the stack

stack.push(*args) #Pushes as many objects as you passed as parameters

stack.pop() #Pops the element on top of the stack and returns it

stack.last() #Returns the item on top of the stack

stack.size() #Returns the size of the stack

stack.is_empty() #Returns whether the stack is empty or not

stack.count(param) #Counts how many items are equal to the one passed as the parameter
```

Module Node
-----------
``` python
from datastructures.graph import Node
```

### Constructor:
``` python
# Node(node_name, value, level, parents)
node = Node("Node name",22,1)
```
### Fields:
``` python

node.value #Any type of value but meant for numbers

node.name #(string)

node.children #(list)

node.level #The level on which the node is located (int)

node.parents #(list)

node.ancestors #(list)

node.paths #All path related to the node (list)
```
## Methods:
``` python
node.get_parents() #(tuple)
node.get_ancestors() #(tuple)
node.get_paths() #(tuple)
```
Module Path
-----------
``` python
from datastructures.graph.path import Path
```
### Constructor:
``` python
path = Path(first_node, second_node, 30) #Path(nodeObjectFrom, nodeObjectTo, weight)
```
** In case you create a path your self: notice that you MUST pass a node OBJECT not its name as you may use when add them in graphs**
### Fields:
``` python
path.first #First node object in the path (start as you wish) (node object)
path.second #(node object)
path.weight #Actually any type of objects but meant for numbers
```
### Methods:
``` python
path.get_opposite(nodeObject) #(node object)
```
Module Graph
------------
``` python
from datastructures.graph.graph import Graph
```
### Constructor:
``` python
graph = Graph()
```
### Fields:
``` python
graph.nodes #All nodes in the graph in format: {"node_name": nodeObject} (dict)
graph.paths #All paths in the graph (list)
```
### Methods:
``` python
graph.add_node(name) #(node object)
graph.connect_nodes(first_node, second_node, weight) #Pass a node object or a node's name and path weight to connect them (path object)
graph.remove_node(name or nodeObject) #(path object)
graph.get_paths() #Returns a stringified visualisation on paths
graph.get_distance(node_from, node_to) # Pass node objects or names and get the shortest distance between them (uses Dijkstra's algorithm so it will only work for paths with positive values) (number)
```
Module Tree
-----------
``` python
from datastructures.graph.tree import Tree
```
### Constructor:
``` python 
#Inherits all fields and methods of Graph
tree = Tree()
```
### Fields:
``` python
tree.structure #The tree's structure in format: {"node_name":[children]} (dict)
tree.children_to_remove #Used when removing a node (list)
tree.names #Names of all nodes in the tree (list)
tree.levels #Number of levels in the tree a.k.a height (int)
```
### Methods:
``` python
tree.add_node(node_name,value,parents(optional),level(optional for nodes on the first level)) #(node object)
tree.get_height() #(int)
tree.get_sturcture() #Returns the tree structure but with name of names instead of their objects (dict)
tree.get_all_nodes_at_level(level) #(tuple)
tree.get_all_nodes() #(tuple)
tree.get_level_info(level) #Returns a string containing the information about a level: the level and nodes at the level (string)
```
