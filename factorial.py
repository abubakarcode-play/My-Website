def factorial(x):
    '''recursing function is being called by itself'''
    if x==0 or x==1:
        return 1 
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))