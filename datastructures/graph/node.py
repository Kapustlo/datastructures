class Node:
    def __init__(self,name,value=None,level=1,parents=[]):
        self.value = value
        self.name = name
        self.children = []
        self.level = level
        self.parents = list(parents)
        self.ancestors = []
        self.ancestors.extend(self.parents)
        self.paths = []
        for parent in self.parents:
            self.ancestors.extend(parent.ancestors)
    def __add__(self, other):
        return self.value + other.value
    def _add_child(self,child):
        self.children.append(child)
    def _remove_child(self,child):
        name = child.name
        for index, child in enumerate(self.children):
            if child.name == name:
                self.children.pop(index)
                break
        return self.children
    def _add_parent(self,parent):
        self.parents.append(parent)
    def get_parents(self):
        return tuple([parent.name for parent in self.parents])
    def get_ancestors(self):
        return tuple([ancestor.name for ancestor in self.ancestors])
    def get_paths(self,node_list=None):
        if node_list != None:
            for index, path in enumerate(self.paths):
                opposite_node = path.get_opposite(self)
                if not opposite_node.name in node_list:
                    self.paths.pop(index)
        return tuple(self.paths)
    def _remove_paths(self,node):
        for index, path in enumerate(self.paths):
            opposite_node = path.get_opposite(self)
            if opposite_node.name == node.name:
                self.paths.pop(index)
        return self.paths
