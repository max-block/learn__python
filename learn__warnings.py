import warnings


class OldClass:
    def __init__(self):
        warnings.warn("this class is deprecated. use a new one", DeprecationWarning, 2)


if __name__ == "__main__":
    o = OldClass()
    print(o)
