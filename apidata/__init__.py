# encoding: utf-8

from functools import wraps


__version = (0, 1, 0)

__version__ = version = '.'.join(map(str, __version))


class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class Apiadmin(Singleton):

    def __init__(self):
        self.method_map = dict()



def api_data(func):
    @wraps(func)
    def _warps(*args, **kwargs):
        api.method_map[func.__name__] = func
        return func(*args, **kwargs)
    return _warps

api = Apiadmin()
