class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Check(metaclass=MetaSingleton):
    pass


if __name__ == '__main__':
    test1 = Check()
    test2 = Check()
    print(test1, '\n', test2)
