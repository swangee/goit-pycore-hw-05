from functools import wraps


def input_error(func, value_error="", key_error="", index_error=""):
    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal value_error, key_error, index_error

        try:
            return func(*args, **kwargs)
        except ValueError:
            return value_error or "value error occurred", False
        except KeyError:
            return key_error or "key error occurred", False
        except IndexError:
            return index_error or "index error occurred", False

    return inner
