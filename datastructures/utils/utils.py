def longest_string(array):
    length = 0 # Default value if the array is empty
    for item in array:
        item_length = len(str(item)) # Number of characters in the string
        if item_length > length:
            length = item_length
    return length # Return the biggest number of characters
