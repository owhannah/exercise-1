# This aims to calculate the product and sum of the two given numbers


# The given interger numbers are
first_number = 20
second_number = 30

# Calculate the product and sum
product = first_number*second_number
sum_result = first_number+second_number

# Return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

if product <=1000:
    result = product
    operation_used = "product"

else: 
     result = sum_result
     operation_used = "sum"

# Display the values of the product, sum, and the result
print(f"Given Number 1: {first_number}")
print(f"Given Number 2: {second_number}")
print(f"Product: {product}")
print(f"Sum: {sum_result}")
print(f"Result ({operation_used}): {result}")