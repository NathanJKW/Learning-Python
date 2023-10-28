"""Examples of user input."""

name = input("What is your name :")
print("Hello", name)

number_1, number_2 = input("Enter two numbers seperated by a space:").split()

number_1 = int(number_1)
number_2 = int(number_2)

SUM = number_1 + number_2

print(SUM)
