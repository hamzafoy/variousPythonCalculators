#Python Script for getting sum of expenses

numOfExpenseRows = int(input("How many rows are on your expense report?\n")) #this retrieves # of expenses user needs to log
expenses = []
sum = 0
for x in range(numOfExpenseRows): #this uses range function to run the input function for each expense needing to be recorded
    expenses.append(float(input("Type out each expense you need to sum up: ")))
for x in expenses: #this loop takes care of adding each expense up to find sum
    sum = sum + x
print("Your expenses total $", sum, sep='')