# https://www.reddit.com/r/learnpython/comments/6sr0i3/how_to_implement_lazy_evaluations_on_numpy_array/dlf1mql?utm_source=share&utm_medium=web2x
from functools import wraps
import numpy as np

operations_chain = []

def lazily_evaluate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        global operations_chain
        operations_chain.append(func, args, kwargs)
    return decorated

np.concat = lazily_evaluate(np.concat)
np.roll = lazily_evaluate(np.roll)
