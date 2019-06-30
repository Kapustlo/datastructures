from datastructures.graph.node import Node
from datastructures.graph.path import Path
from math import inf as Infinity

class Graph:
    def __init__(self):
        """
        self.nodes format:
        {
            "node_name": nodeObject
        }
        """
        self.nodes = {}
        self.paths = [] # Path objects
    def __iter__(self):
        return iter([self.nodes[node] for node in self.nodes])
    def get_node(self,name):
        type_name = type(name).__name__
        if type_name == 'Node':
            return name
        else:
            return self.nodes[str(name)]
    def add_node(self,name):
        node = Node(name)
        self.nodes[str(name)] = node
        return node
    def connect_nodes(self,first,second,weight):
        first = self.get_node(first)
        second = self.get_node(second)
        path = Path(first,second,weight)
        first.paths.append(path)
        second.paths.append(path)
        self.paths.append(path)
        return path
    def remove_node(self,node):
        node = self.get_node(node)
        for index, path in enumerate(self.paths):
            # Find all paths containing this node and remove them
            if path.first.name == node.name or path.second.name == node.name:
                self.paths.pop(index)
        del self.nodes[node.name]
        for path in node.paths:
            opposite_node = path.get_opposite(node)
            opposite_node._remove_paths(node)
        del node
        return self.paths
    def get_paths(self):
        result = ""
        for path in self.paths:
            result += "{} <---> {} = {}\n".format(path.first.name,path.second.name,path.weight)
        return result
    def _mod_table(self,table,current,to,visited=[]):
        # Dijkstra's algorithm
        visited.append(current.name)
        smallest_weight = Infinity
        current_node = current # Assign the given node first not to get a random erro
        for path in current.paths:
            opposite_node = path.get_opposite(current)
            # So here we just basically count how much it costs to move from the start to this node
            cur_length = path.weight + table[current.name]
            # The nodes current table value aka how much it costs to get here from the start
            table_value = table[opposite_node.name]
            if table_value > cur_length:
                table[opposite_node.name] = cur_length
            if smallest_weight > cur_length and not opposite_node.name in visited:
                smallest_weight = cur_length
                current_node = opposite_node
        if len(visited) == len(self.nodes.keys()) or current_node.name in visited:
            # If we have visited all nodes in the graph, return table value
            return table
        else:
            return self._mod_table(table,current_node,to,visited)
    def get_distance(self,node_from,node_to):
        # Dijkstra's algorithm
        node_from = self.get_node(node_from)
        node_to = self.get_node(node_to)
        # Create table that show distance from the start to every other node in the graph
        table = {node: Infinity for node in self.nodes}
        table[node_from.name] = 0
        return self._mod_table(table,node_from,node_to)[node_to.name]
