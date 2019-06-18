# rjk Tools
Misc tools to help with programming more efficently

 	

## decorators
### Example of the dynamic_programming usage on a fibonachi function
~~~~
@dynamic_programming
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)	

~~~~