class Path:
    def __init__(self,first,second,weight):
        self.first = first
        self.second = second
        self.weight = weight
    def get_opposite(self,node):
        if node.name == self.first.name:
            return self.second
        else:
            return self.first
