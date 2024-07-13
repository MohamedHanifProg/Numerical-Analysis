 # questions 9-11                   
from math import factorial, sqrt, pi

# 1. Compute 6!
factorial_6 = factorial(6)

# 2. Compute the number of leap years between the years 1500 and 2010
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

leap_years = [year for year in range(1500, 2011) if is_leap_year(year)]
num_leap_years = len(leap_years)

# 3. Approximation for π using Ramanujan's formula
def ramanujan_pi_approximation(N):
    sum_term = sum((factorial(4*k) * (1103 + 26390*k)) / ((factorial(k) ** 4) * (396 ** (4*k))) for k in range(N+1))
    approximation = (2 * sqrt(2) / 9801) * sum_term
    return 1 / approximation

# Using N = 10 for a decent approximation
N = 10
ramanujan_pi = ramanujan_pi_approximation(N)

print("6! =", factorial_6)
print("Number of leap years between 1500 and 2010 =", num_leap_years)
print("Ramanujan's approximation of π =", ramanujan_pi)
# question 13-14                    
import math

# Values of x to verify sin^2(x) + cos^2(x) = 1
x_values = [math.pi, math.pi/2, math.pi/4, math.pi/6]

# Verify sin^2(x) + cos^2(x) = 1 for given x values
verification_results = [(x, math.sin(x)**2 + math.cos(x)**2) for x in x_values]

# Print results
for x, result in verification_results:
    print(f"sin^2({x}) + cos^2({x}) = {result}")

# Compute sin(87°)
sin_87_degrees = math.sin(math.radians(87))
print(f"sin(87°) = {sin_87_degrees}")

# questions 19-22       
# Define the logical operations
def logical_or(P, Q):
    return not (not P and not Q)

def logical_and(P, Q):
    return not (not P or not Q)

def logical_xor(P, Q):
    return (P or Q) and not (P and Q)

# Test values for P and Q
test_values = [(False, False), (False, True), (True, False), (True, True)]

# Check the conditions for (P AND Q) OR (P AND (NOT Q)) being false
def condition_false(P, Q):
    return (P and Q) or (P and not Q)

# Output the results
print("Testing (P AND Q) OR (P AND (NOT Q))")
for P, Q in test_values:
    result = condition_false(P, Q)
    print(f"P = {P}, Q = {Q} => (P AND Q) OR (P AND (NOT Q)) = {result}")

print("\nTesting logical OR using AND and NOT")
for P, Q in test_values:
    result = logical_or(P, Q)
    print(f"P = {P}, Q = {Q} => P OR Q = {result}")

print("\nTesting logical AND using OR and NOT")
for P, Q in test_values:
    result = logical_and(P, Q)
    print(f"P = {P}, Q = {Q} => P AND Q = {result}")

print("\nTesting logical XOR using AND, OR, and NOT")
for P, Q in test_values:
    result = logical_xor(P, Q)
    print(f"P = {P}, Q = {Q} => P XOR Q = {result}")

    # questions of section 2    
# Assign the strings 'HELLO' and 'hello' to s1 and s2 respectively
s1 = 'HELLO'
s2 = 'hello'

# Use the == operator to compare s1 and s2 directly
equal_direct = s1 == s2
print(f"s1 == s2: {equal_direct}")

# Use the == operator to compare s1.lower() and s2
equal_lower = s1.lower() == s2
print(f"s1.lower() == s2: {equal_lower}")

# Use the == operator to compare s1 and s2.upper()
equal_upper = s1 == s2.upper()
print(f"s1 == s2.upper(): {equal_upper}")
# %whos this command will show them in the jupiter notebook     
# Generate strings
print("The word 'Engineering' has", len('Engineering'), "letters.")
print("The word 'Book' has", len('Book'), "letters.")

# Check if 'Python' is in 'Python is great!'
if 'Python' in 'Python is great!':
    print("'Python' is in 'Python is great!'")
else:
    print("'Python' is not in 'Python is great!'")

# Get the last word 'great' from 'Python is great!'
sentence = 'Python is great!'
last_word = sentence.split()[-1]
print("The last word in 'Python is great!' is:", last_word)

# Assign list [1, 8, 9, 15] to a variable list_a
list_a = [1, 8, 9, 15]
# Insert 2 at index 1 using the insert method
list_a.insert(1, 2)
# Append 4 to list_a using the append method
list_a.append(4)

# Sort list_a in ascending order
list_a.sort()
print("Sorted list_a:", list_a)

import numpy as np

# Generate an array with size 100 evenly spaced between -10 to 10
array_100 = np.linspace(-10, 10, 100)

# Let array_a be an array [-1, 0, 1, 2, 0, 3]
array_a = np.array([-1, 0, 1, 2, 0, 3])
# Return an array consisting of all elements of array_a that are larger than zero
positive_elements = array_a[array_a > 0]

# Create an array y = [[3, 2, 3], [5, 2, 8], [3, 5, 9]]
y = np.array([[3, 2, 3], [5, 2, 8], [3, 5, 9]])
# Calculate the transpose of the array
y_transpose = np.transpose(y)

# Create a zero array with size (2, 4)
zero_array = np.zeros((2, 4))

# Change the 2nd column in the above array to 1
zero_array[:, 1] = 1
#%reset -f


