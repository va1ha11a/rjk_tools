def __string_args_key_gen(*args, **kwargs):
    """
    Key gen function for dynamic programming.
    Will create a string from args. Some issues might be seen with
    deep data types if order is not consistant.
    """
    key = (str(args), str(sorted(kwargs)),
           str([kwargs[k] for k in sorted(kwargs)]))
    return key


def dynamic_programming(func):
    """
    Decorator function that should be able to wrap many functions to make them
    dynamic programming / memoisation.

    Functions should be pure and not have external factors (such as external web calls)
    as this could give incorrect results.
    """
    # TODO: Check safty accross many functions using it simutainously. I belive this should be ok
    # as the closure containse the _store and I have checked a simple example.

    # TODO: Add other backends such as flatfile or db as options
    _store = {}
    key_func = __string_args_key_gen

    def inner(*args, **kwargs):
        key = key_func(args, kwargs)
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
