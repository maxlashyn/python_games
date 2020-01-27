""" unit testing """
""" packages for testing """

""" doctest """

"""
>>> append(2,3)
5
"""
def append(x, y):
    return x - y

if __name__ == '__main__':
    import doctest
    doctest.testmod()
