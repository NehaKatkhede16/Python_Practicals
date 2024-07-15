# study & demonstrate Dictionay in python and write a program, on working dictionaries in python.

#create & print a dictionary 
Dict = {1: 'Neha', 2: 'Priya', 3: 'Sakshi'}
print(Dict)

#print type of a dictionary
thisdict = {
    "brand":"ford",
    "model":"mustang",
    "Year":1965
}
print(type(thisdict))

#accessing item
thisdict = {
    "brand":"ford",
    "model":"mustang",
    "Year":1965
}
x = thisdict["brand"]
print(x)

#get 
x = thisdict.get("model")
print(x)


#keys
x = thisdict.keys()
print(x)



