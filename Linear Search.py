def linear_search(data, search_item):
    """
    Perform linear search on a list to find the index of a given search item.

    Parameters:
    data (list): The list to be searched.
    search_item: The item to be searched for.

    Returns:
    int: The index of the search item if found, -1 otherwise.
    """
    for index, item in enumerate(data):
        if item == search_item:
            return index
    return -1

data = ["Philip", "Boris", "Kevin", "Alvin", "David"]
search_item = input("Enter the item to search: ")
position = linear_search(data, search_item)
if position != -1:
    
    print(f"The item is found at position {position + 1}")
else:
    print("The item is not found")

