from datastructures.graph.node import Node
from datastructures.graph.graph import Graph
from datastructures.utils.utils import longest_string
class Tree(Graph):
    def __init__(self):
        super()
        """
            self.structure format:
            {
                "node_name": [childrenObjects]
            }
        """
        self.structure = {}
        self.children_to_remove = []
        self.names = []
        self.levels = 0
    def add_node(self,name,value,parents=[],level=None):
        if not level:
            if len(parents):
                level = parents[0].level + 1
            else:
                level = 1
        # If the node is not on top, then it needs parents
        if (level > 1 and len(parents) == 0) or self.names.count(name) > 0:
            raise ValueError("A node must have a parent if its level is greater than 1")
        else:
            for index, parent in enumerate(parents):
                # Parent must not be lower than child
                if parent.level >= level:
                    raise ValueError("Parent must not be lower than its children")
                else:
                    # In case there is a string, we call this method
                    parents[index] = self.get_node(parent)
            # Creating a new node
            node = Node(name,value,level,parents)
            for index, parent in enumerate(parents):
                parent._add_child(node)
            try:
                # Trying to append it into an existing list of nodes
                self.structure[str(level)].append(node)
            except:
                # Creating a new list of nodes if it's not created yet
                self.structure[str(level)] = [node]
            self.names.append(name)
            self.levels = len(self.structure.keys())
            return node
    def get_height(self):
        return self.levels
    def remove_node(self,node):
        node = self.get_node(node)
        name = node.name
        names_index = self.names.index(name)
        del self.names[names_index]
        level = self.structure[str(node.level)]
        for index, node in enumerate(level):
            if node.name == name:
                for child in node.children:
                    if len(child.parents) - 1 == 0:
                        self.children_to_remove.append(child)
                for parent in node.parents:
                    parent._remove_child(node)
                level.pop(index)
                if len(level) == 0:
                    del self.structure[str(node.level)]
                break
        if len(self.children_to_remove):
            self.remove_node(self.children_to_remove.pop(0))
        else:
            return self.structure
    def get_structure(self):
        # So, this basically return the regular structure but with node names insteas of node objects as values
        result = {}
        for level in self.structure:
            nodes = self.structure[level]
            result[level] = [node.name for node in nodes]
        return result
    def get_all_nodes_at_level(self,level):
        return tuple(self.structure[str(level)])
    def get_all_nodes(self):
        result = []
        for level in self.structure:
            value = self.structure[level]
            result.extend(value)
        return tuple(result)
    def get_level_info(self,level):
        node_list = self.get_all_nodes_at_level(level)
        level = "Current level: " + str(level)
        nodes_at_level = "Nodes at current level: " + str(len(node_list))
        nodes = "Nodes: " + str([node.name for node in node_list])
        l_s = longest_string((level,nodes_at_level,nodes))
        floor = roof = "-" * (l_s + 2)
        return "{}\n{}\n{}\n{}\n{}".format(roof,level,nodes_at_level,nodes,floor)
