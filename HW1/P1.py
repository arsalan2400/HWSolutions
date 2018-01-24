
# Question 1: Object types
# Consider the number 17. Construct multiple variables (y1, y2, y3, and y4) in Python that
# represent the 17 in the various forms of objects (ints, floats, strings, and boolean).
# (Hint: For creation of the Boolean, set a value for 17 to be compared against.)
# Use y1, y2, or y3 to create a variable named text such that print(text) prints 'The value of x is 17'

# setting x = 17
x = 17
print('Setting x =', x)

# naturally, x is an 'int'
y1 = x
print('Setting y1 = x results in y1 =', y1, '| Type of y1:', type(y1))

# float
y2 = float(x)
print('Setting y2 = float(x) results in y2 =', y2, '| Type of y2:', type(y2))

# string
y3 = str(x)
print('Setting y3 = str(x) results in y3 =', y3, '| Type of y3:', type(y3))

# Boolean, here '17 < 14' is being evaluated
y4 = bool(x < 14)
print('Setting y4 = bool(x < 14) results in y4 =', y4, '| Type of y4:', type(y4))

# print
text = 'The value of x is ' + y3
print(text)







