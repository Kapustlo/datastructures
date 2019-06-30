class Path:
    def __init__(self,first,second,weight):
        self.first = first
        self.second = second
        self.weight = weight
    def get_opposite(self,node):
        node_name = node.name
        if node_name == self.first.name:
            return self.second
        elif node_name == self.second.name:
            return self.first
