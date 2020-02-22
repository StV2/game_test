import functools
import inspect
from helper import ALLOWABLE_TYPES

def typechecked(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before

        stack = inspect.stack()

        for arg in args[1:]:
            if type(arg) not in ALLOWABLE_TYPES[func.__name__]:
                raise TypeError("at line {lineno} in {caller}: expected {allowed_types}, got {actual_type} instead".format(lineno = stack[1].lineno, caller=stack[1].function, allowed_types=ALLOWABLE_TYPES[func.__name__], actual_type=type(arg)))

        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator