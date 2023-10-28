"""Examples of casting from one data type to another."""

# Casting
# Casting allows you to convert from one type to another. Here is how you cast to the different
# types. I’ll use the type() function to display the new data type for each variable.

INTERGER_TYPE = 1
FLOAT_TYPE = 1.1
COMPLEX_TYPE = 1.23j
STRING_TYPE = "5"

print("Cast interger to float", type(float(INTERGER_TYPE)))
print("Cast float to interger", type(int(FLOAT_TYPE)))
print("Cast complex to interger", type(str(COMPLEX_TYPE)))
print("Cast string to complex", type(complex(STRING_TYPE)))
