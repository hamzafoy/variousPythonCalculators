# Basic Hello World statement printed
print("Hello World!")

# Build a List using user input, print one to the terminal.
print("Enter three country names of your choice!")
userProvidedValues = [input(), input(), input()]
print(userProvidedValues[1], "is the second country you submitted!")

# Build a dictionary of three-country lists using user's previous input & a predetermined from computer.
countries = {'user': userProvidedValues, 'comp': ['Italy', 'Mozambique', 'Pakistan']}
print(countries[input("Type 'user' to see countries you listed, 'comp' to see the computers' preferred country ")])

# Build a tuple and print on of the values.
exampleTuple = (12.6667, 10260, "Aragorn", [1,2,3])
print(exampleTuple[3])