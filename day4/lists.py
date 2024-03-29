# Methods of list objects:

fruits = ["Cherry", "Apple"]

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
fruits.append("Watermelon")

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
fruits.extend(["Pear", "Apple", "Orange"])

# list.insert(i, x)
# Insert an item at a given position. 
# The first argument is the index of the element before which to insert, 
# so a.insert(0, x) inserts at the front of the list, 
# and a.insert(len(a), x) is equivalent to a.append(x).
fruits.insert(3, "Banana")

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
fruits.remove("Apple")

# list.pop([i])
# Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list. 
# It raises an IndexError if the list is empty or the index is outside the list range.
fruits.pop()
fruits.pop(0)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].
fruits.clear()

# Extend new items
fruits.extend(["Banana", "Pear", "Orange", "Banana"])

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.
print(f'Orange Index: {fruits.index("Orange")}')

# list.count(x)
# Return the number of times x appears in the list.
print(f'Number of items "Bananas": {fruits.count("Banana")}')

# list.sort(*, key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
fruits.sort()
print(f"Sort list: {fruits}")

# list.reverse()
# Reverse the elements of the list in place.
fruits.reverse()
print(f"Reverse list: {fruits}")

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].
shopping_list = fruits.copy()
print(f"This is my shopping list: {shopping_list}")

# Create a list from a String of characters using the split() method. And print a random name y the created new list
import random
names = "John, Mary, Ella, Alex, Tony, Kevin"
names_list = names.split(", ")
random_index = random.randint(0, (len(names_list) - 1)) # Create a random Index
print(names_list[random_index]) # Print a random name in names_list

