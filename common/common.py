from functools import wraps
from time import time


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec with args: [%r, %r]' % (f.__name__, te - ts, args, kw))
        return result

    return wrap
