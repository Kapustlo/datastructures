from datastructures.utils import utils
class Stack:
    def __init__(self,*args):
        self.items = list(args) # All our stack items are stored here
    def get_stack(self):
        longest_string = utils.longest_string(self.items)
        max_spaces = " " * longest_string # Here we create spaces to fill the gap between | and | so it looks beautiful
        floor = "_" * longest_string # Floor is basically the same as max_spaces but with "_" instead of spaces
        roof = "-" * longest_string # No comments
        string = "" # The prettyfied stack visualisation
        for index, item in enumerate(self.items):
            item = str(item)
            item_length = len(item)
            middle_spaces = (longest_string // 2) - (item_length // 2) # Here we calculate how many spaces we need in order to place the string in the middle
            middle_spaces_str = " " * middle_spaces # Add the actual spaces from the left
            spaces = longest_string - item_length - middle_spaces # calculate spaces from the right
            spaces_str = " " * spaces # Add the actual spaces from the right
            # If it's the first item then we print the "roof", otherwise spaces
            if index == 0:
                top = roof
            else:
                top = max_spaces
            string += "|{}|\n|{}{}{}|\n|{}|\n".format(top,middle_spaces_str,item,spaces_str,floor)
        return string
    def get_all_as_list(self):
        return self.items # After everything I typed above you are going to use this?
    def push(self,*args):
        for arg in args:
            self.items.append(arg)
        return self.items
    def pop(self):
        return self.items.pop()
    def last(self):
        length = len(self.items)
        if length:
            return self.items[length - 1]
        else:
            return None
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items == []
    def count(self,param):
        return self.items.count(param)
