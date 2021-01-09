# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        #  n = n*n-1*n-2     
        return n * factorial(n - 1)
    

print(factorial(10))
# => 120