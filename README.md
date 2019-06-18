# rjk Tools
Misc tools to help with programming more efficently

 	

## decorators
### Example of the dynamic_programming usage on a fibonacci function
```python
from rjk_tools.decorators import dynamic_programming

@dynamic_programming
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)	
```



### Example of results:
```python
>>>fib(8)
>>>21
```
#### Without the decorator the following functioncalls would be made:
fib(8),fib(7),fib(6),fib(5),fib(4),fib(3),fib(2),fib(1),fib(0),fib(1),fib(2),fib(1),fib(0),fib(3),fib(2),fib(1),fib(0),fib(1),fib(4),fib(3),fib(2),fib(1),fib(0),fib(1),fib(2),fib(1),fib(0),fib(5),fib(4),fib(3),fib(2),fib(1),fib(0),fib(1),fib(2),fib(1),fib(0),fib(3),fib(2),fib(1),fib(0),fib(1),fib(6),fib(5),fib(4),fib(3),fib(2),fib(1),fib(0),fib(1),fib(2),fib(1),fib(0),fib(3),fib(2),fib(1),fib(0),fib(1),fib(4),fib(3),fib(2),fib(1),fib(0),fib(1),fib(2),fib(1),fib(0)

#### With the decorator it is reduced to:
fib(8),fib(7),fib(6),fib(5),fib(4),fib(3),fib(2),fib(1),fib(0)

#### Subsequent runs only run previously unrun calls.
```python
>>>fib(9)
>>>34
```
#### The above only will run:
fib(9)