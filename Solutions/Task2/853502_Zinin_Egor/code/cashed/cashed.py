import json
import os.path


def cached(func):
    d = {}
    if os.path.exists('file.json'):
        with open('file.json') as f:
            d = json.load(f)

    def wrapped(*args, **kwargs):
        if d.get('{}'.format(args, kwargs)) is None:
            d['{}'.format(args, kwargs)] = func(*args, **kwargs)
        with open('file.json', 'w') as f:
            json.dump(d, f)

        return d.get('{}'.format(args, kwargs))

    return wrapped


@cached
def mul(a, b):
    return a * b
