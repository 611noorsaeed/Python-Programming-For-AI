# 1 Arithematic Operators:
# Define variables
a = 8
b = 4

# Perform arithmetic operations
sum_result = a + b
diff_result = a - b
product_result = a * b
quotient_result = a / b
floor_div_result = a // b
modulus_result = a % b
exponent_result = a ** b

# Display results
print(f"The sum of {a} and {b} is {sum_result}")
print(f"The difference between {a} and {b} is {diff_result}")
print(f"The product of {a} and {b} is {product_result}")
print(f"The quotient of {a} divided by {b} is {quotient_result}")
print(f"The floor division of {a} by {b} is {floor_div_result}")
print(f"The modulus of {a} and {b} is {modulus_result}")
print(f"The result of {a} raised to the power of {b} is {exponent_result}")


print("\n\n======================\n\n")

# 2 Comparison Operators
# Define variables
a = 8
b = 4

# Perform comparison operations
equal_result = (a == b)
not_equal_result = (a != b)
greater_than_result = (a > b)
less_than_result = (a < b)
greater_equal_result = (a >= b)
less_equal_result = (a <= b)

# Display results
print(f"Is {a} equal to {b}? {equal_result}")
print(f"Is {a} not equal to {b}? {not_equal_result}")
print(f"Is {a} greater than {b}? {greater_than_result}")
print(f"Is {a} less than {b}? {less_than_result}")
print(f"Is {a} greater than or equal to {b}? {greater_equal_result}")
print(f"Is {a} less than or equal to {b}? {less_equal_result}")

print("\n\n======================\n\n")

# 3 Logical Operators
# Define variables
a = True
b = False

# Perform logical operations
and_result = a and b
or_result = a or b
not_a_result = not a
not_b_result = not b
# Display results
print(f"The result of {a} and {b} is {and_result}")
print(f"The result of {a} or {b} is {or_result}")
print(f"The result of not {a} is {not_a_result}")
print(f"The result of not {b} is {not_b_result}")


print("\n\n================")
# 4 Membership Operators

# Define variables
sequence = [1, 2, 3, 4, 5]
element1 = 3
element2 = 6

# Perform membership operations
in_result1 = element1 in sequence
in_result2 = element2 in sequence
not_in_result1 = element1 not in sequence
not_in_result2 = element2 not in sequence


# Display results
print(f"Is {element1} in {sequence}? {in_result1}")
print(f"Is {element2} in {sequence}? {in_result2}")
print(f"Is {element1} not in {sequence}? {not_in_result1}")
print(f"Is {element2} not in {sequence}? {not_in_result2}")


print("\n\n=====================")
# 5 Identity opertors
# Example variables
a = [1, 2, 3]
b = [1, 2, 3]
c = a

# Using `is`
print(a is b)   # False, as a and b are different objects
print(a is c)   # True, as a and c refer to the same object

# Using `is not`
print(a is not b)  # True, as a and b are different objects
print(a is not c)  # False, as a and c refer to the same object

