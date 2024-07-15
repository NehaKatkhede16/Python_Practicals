# a) To study and demonstrate list in python.
# b) WAP to write, append & remove list.



# Creating a list
my_list = [1, 2, 3, 'apple', 'banana', True, 3.14]
print(my_list)




 #b) WAP to write, append & remove list.
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)

# using append method
numbers.append(32)
print("After Append:", numbers)

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Python' from the list
languages.remove('Python')

print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']