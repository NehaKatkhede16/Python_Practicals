# study & demonstarte python condition & if statement.
# WAP a program to convert tempretures to & from celcius, farenhit. [formula: c/5 f-32/9]


#study & demonstarte python condition & if statement.
number = 10
# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement.')

#if else
number = 10
if number > 0:
    print('Positive number')
else:
    print('Negative number')
print('This statement is if else')

#nested if
x=41
if x>10:
   print("Above ten")
if x>20:
   print("and also above 20!")
else:
   print("but not above20.")



# Python Program to convert temperature in celsius to fahrenheit
# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
