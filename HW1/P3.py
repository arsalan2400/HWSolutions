# Question 3: Fibonacci sequence


# iterative version:
def fibonacci_iterative(n):
    n_minus_1 = 1
    n = 1

    for i in range(n):
        result =
    if n == 0 or n ==1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# recursive version:
def fibonacci_recursive(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)



n = int(input('Enter # of terms:'))
print('Fibonacci sequence:')
print(fibonacci(n))

# function
def fibFunction(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibFunction(n-1) + fibFunction(n-2)

print(fibFunction(23))
