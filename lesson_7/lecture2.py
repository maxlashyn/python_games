""" unit testing """
""" packages for testing """

""" doctest """


def append(x, y):
    """
    >>> append(2,3)
    5
    >>> append(1, 3)
    4
    >>> append([1, 2], [2, 3])
    [1, 2, 2, 3]
    """
    return x + y


if __name__ == '__main__':
    import doctest

    doctest.testmod()
