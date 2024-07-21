import numpy as np

# Question 1: Hyperbolic Sine Function
def my_sinh(x):
    """
    Compute the hyperbolic sine of x.
    :param x: A 1 by 1 float.
    :return: The hyperbolic sine of x.
    """
    return (np.exp(x) - np.exp(-x)) / 2

# Test Cases for Question 1
print(my_sinh(0))    # 0
print(my_sinh(1))    # 1.1752
print(my_sinh(2))    # 3.6269

# Question 2: Checker Board Matrix
def my_checker_board(n):
    """
    Create an n by n checker board matrix.
    :param n: A strictly positive integer.
    :return: An n by n array with a checkerboard pattern.
    """
    m = np.zeros((n, n), dtype=int)
    m[::2, ::2] = 1
    m[1::2, 1::2] = 1
    return m

# Test Cases for Question 2
print(my_checker_board(1))  
print(my_checker_board(2))  
print(my_checker_board(3))  
print(my_checker_board(5))  

# Question 3: Triangle Area
def my_triangle(b, h):
    """
    Compute the area of a triangle given its base and height.
    :param b: The base of the triangle.
    :param h: The height of the triangle.
    :return: The area of the triangle.
    """
    return 0.5 * b * h

# Test Cases for Question 3
print(my_triangle(1, 1))    # 0.5
print(my_triangle(2, 1))    # 1
print(my_triangle(12, 5))   # 30

# Question 4: Split Matrix
def my_split_matrix(m):
    """
    Split a matrix into two halves.
    :param m: An array with at least two columns.
    :return: A list [m1, m2] where m1 is the left half and m2 is the right half.
    """
    cols = m.shape[1]
    mid = (cols + 1) // 2
    m1 = m[:, :mid]
    m2 = m[:, mid:]
    return m1, m2

# Test Cases for Question 4
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  
m1, m2 = my_split_matrix(m)
print(m1)
print(m2)

m = np.ones((5, 5))
m1, m2 = my_split_matrix(m)
print(m1)
print(m2)

# Question 5: Cylinder Surface Area and Volume
def my_cylinder(r, h):
    """
    Compute the surface area and volume of a cylinder.
    :param r: The radius of the cylinder.
    :param h: The height of the cylinder.
    :return: A list [s, v] where s is the surface area and v is the volume.
    """
    s = 2 * np.pi * r**2 + 2 * np.pi * r * h
    v = np.pi * r**2 * h
    return [s, v]

# Test Cases for Question 5
print(my_cylinder(1, 5))    # [37.6991, 15.7080]
print(my_cylinder(2, 4))    # [62.8319, 37.6991]

# Question 6: Count Odd Numbers
def my_n_odds(a):
    """
    Count the number of odd numbers in an array.
    :param a: A one-dimensional array of floats.
    :return: The number of odd numbers in the array.
    """
    return np.sum(a % 2 != 0)

# Test Cases for Question 6
print(my_n_odds(np.arange(100)))    # 50
print(my_n_odds(np.arange(2, 100, 2)))    # 0

# Question 7: Array of Twos
def my_twos(m, n):
    """
    Create an m by n array filled with the value 2.
    :param m: Number of rows.
    :param n: Number of columns.
    :return: An m by n array filled with twos.
    """
    return np.full((m, n), 2)

# Test Cases for Question 7
print(my_twos(3, 2))   
print(my_twos(1, 4))   

# Question 8: Lambda Function for Subtraction
sub = lambda x, y: x - y

# Example usage for Question 8
print(sub(10, 5))    # 5

# Question 9: String Concatenation
def add_string(s1, s2):
    """
    Concatenate two strings.
    :param s1: The first string.
    :param s2: The second string.
    :return: The concatenated string.
    """
    return s1 + s2

# Test Cases for Question 9
s1 = add_string('Programming', ' ')
s2 = add_string('is', ' fun!')
print(add_string(s1, s2))    # 'Programming is fun!'

# Question 10: Generate Errors
# TypeError example
def fun(a):
    pass

# Uncomment to see the error
# fun()

# IndentationError example
def fun():
#     print("This will cause an indentation error")
    pass

# Uncomment to see the error
# fun()

# Question 11: Greeting Function
def greeting(name, age):
    """
    Return a greeting message with name and age.
    :param name: The name as a string.
    :param age: The age as a float.
    :return: A greeting string.
    """
    return f"Hi, my name is {name} and I am {age} years old."

# Test Cases for Question 11
print(greeting('John', 26))    # 'Hi, my name is John and I am 26 years old.'
print(greeting('Kate', 19))    # 'Hi, my name is Kate and I am 19 years old.'

# Question 12: Donut Area
def my_donut_area(r1, r2):
    """
    Compute the area outside the circle with radius r1 and inside the circle with radius r2.
    :param r1: Radius of the inner circle.
    :param r2: Radius of the outer circle.
    :return: The area of the donut-shaped region.
    """
    return np.pi * (r2**2 - r1**2)

# Test Cases for Question 12
print(my_donut_area(np.arange(1, 4), np.arange(2, 7, 2)))    # [9.4248, 37.6991, 84.8230]

# Question 13: Within Tolerance
def my_within_tolerance(A, a, tol):
    """
    Find indices of elements in A such that |A - a| < tol.
    :param A: A one-dimensional float list or array.
    :param a: The reference value.
    :param tol: The tolerance value.
    :return: A list of indices.
    """
    return np.where(np.abs(A - a) < tol)[0]

# Test Cases for Question 13
print(my_within_tolerance([0, 1, 2, 3], 1.5, 0.75))    # [1, 2]
print(my_within_tolerance(np.arange(0, 1.01, 0.01), 0.5, 0.03))    # [47, 48, 49, 50, 51, 52]

# Question 14: Bounding Array
def bounding_array(A, top, bottom):
    """
    Bound the values in array A within the given top and bottom limits.
    :param A: A one-dimensional float array.
    :param top: The upper bound.
    :param bottom: The lower bound.
    :return: The bounded array.
    """
    A = np.array(A)
    A[A > top] = top
    A[A < bottom] = bottom
    return A

# Test Cases for Question 14
print(bounding_array(np.arange(-5, 6, 1), 3, -3))    # [-3, -3, -3, -2, -1, 0, 1, 2, 3, 3, 3]
