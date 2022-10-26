numbers = []  # variable = empty array fields
strings = []
names = ['John', 'Eric', 'Jessica']  # sets integer to the 'names' variable
# places & displays the number 1 from info found in  the parentheses.
numbers.append(1)
numbers.append(2)
numbers.append(3)
# places & displays a string in series gathered from info in the parentheses.
strings.append('Hello')
strings.append('World')
# takes and displays the second name from the 'names' variable array
second_name = names[1]
print(numbers)
print(strings)
# %s specifically is used to perform concatenation of strings together. It allows us to format a value inside a string
print('The second name on the names list %s' % second_name)
