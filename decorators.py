def dynamic_programming(func):
    """
    Decorator function that should be able to wrap many functions to make them
    dynamic programming / memoisation.

    Functions should be pure and not have external factors (such as external web calls)
    as this could give incorrect results.
    """
    _store = {}

    def inner(*args, **kwargs):
        key = (args, tuple(sorted(kwargs)), tuple(
            [kwargs[k] for k in sorted(kwargs)]))
        prev = _store.get(key)
        if prev != None:
            # 'returning from cache'
            return prev
        else:
            # 'new calculation'
            ret = func(*args, **kwargs)
            _store[key] = ret
            return ret
    return inner

# Example:
# @dynamic_programming
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)