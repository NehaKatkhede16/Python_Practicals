# study & demonstrate tuples in python, write a program to demonstrate working with tuples in python.

# Creating a tuple
my_tuple = ("apple", "banana", "cherry")

# Accessing elements of a tuple
print("The first element of the tuple is:", my_tuple[0])
print("The second element of the tuple is:", my_tuple[1])
print("The third element of the tuple is:", my_tuple[2])

# Concatenating tuples
new_tuple = my_tuple + ("dates", "elderberry")
print("The new tuple after concatenation is:", new_tuple)

# Deleting a tuple
del new_tuple
try:
    print(new_tuple)
except NameError:
    print("The tuple has been deleted.")
