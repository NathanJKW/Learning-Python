"""Available data types in python."""

# Dynamic Typing
# Python is dynamically typed. What that means is a variables data type is determined by the
# value you assign to it. This is different from other languages. A variables value can also be
# changed even if that may sometimes not make sense. For example

MY_AGE = 43
MY_AGE = "Dog"

# Many errors can occur if you don’t make sure you are using the correct values. Some times you
# will find the need to convert from one type to another.

# Numerical Data Type

# create a variable with integer value.
INTERGER_TYPE = 100
print("The type of variable having value",
      INTERGER_TYPE, " is ", type(INTERGER_TYPE))

# create a variable with float value.
FLOAT_TYPE = 10.2345
print("The type of variable having value",
      FLOAT_TYPE, " is ", type(FLOAT_TYPE))

# create a variable with complex value.
COMPLEX_TYPE = 100+3j
print("The type of variable having value",
      COMPLEX_TYPE, " is ", type(COMPLEX_TYPE))

# String Data Type

STRING_TYPE_A = "string in a double quote"
STRING_TYPE_B = 'string in a single quote'
print(STRING_TYPE_A)
print(STRING_TYPE_B)

# using ',' to concatenate the two or several strings
print(STRING_TYPE_A, "concatenated with", STRING_TYPE_B)

# using '+' to concate the two or several strings
print(STRING_TYPE_A+" concated with "+STRING_TYPE_B)

# Python List Data Type

# list of having only integers
LIST_TYPE_A = [1, 2, 3, 4, 5, 6]
print(LIST_TYPE_A)

# list of having only strings
LIST_TYPE_B = ["hello", "john", "reese"]
print(LIST_TYPE_B)

# list of having both integers and strings
LIST_TYPE_C = ["hey", "you", 1, 2, 3, "go"]
print(LIST_TYPE_C)

# index are 0 based. this will print a single character
print(LIST_TYPE_C[1])  # this will print "you" in list LIST_TYPE_C

# Tuple Data Type

# tuple having only integer type of data.
TULIP_TYPE_A = (1, 2, 3, 4)
print(TULIP_TYPE_A)  # prints the whole tuple

# tuple having multiple type of data.
TULIP_TYPE_B = ("hello", 1, 2, 3, "go")
print(TULIP_TYPE_B)  # prints the whole tuple

# index of tuples are also 0 based.

# this prints a single element in a tuple, in this case "go"
print(TULIP_TYPE_B[4])
