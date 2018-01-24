# Problem 3. Iterative and recursive operations.
# Write an iterative function and a recursive function that
# computes the sum of all numbers from 1 to n, where n is given as parameter.
# Test both functions for n = 100.

# iterative version:
def sum_iterative(n):

    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


# recursive version:
def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n-1)


# test iterative version of sum
print(sum_iterative(100))
# test recursive version of sum
print(sum_recursive(100))
