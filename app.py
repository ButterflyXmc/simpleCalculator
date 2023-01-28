# importing files
import add
import subtract
import multiply
import divide

print("Let's play with numbers! Please select from the following operations :-")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
# print("Please enter your selection :")

#! ...................................

# user's selection
selection = input("Please enter your selection :")

#user's first number 
first = int(input("Enter the first number :"))

#user's second number
second = int(input("Enter the second number :"))

if selection == "1":
    print("Your answer is :")
    print(add.addition(first,second))
elif selection == "2":
    print("Your answer is :")
    print(subtract.subtract(first,second))
elif selection == "3":
    print("Your answer is :")
    print(multiply.multiply(first,second))
elif selection == "4":
    print("Your answer is :")
    print(divide.division(first,second))
else:
    print("Please enter a valid operation!")
