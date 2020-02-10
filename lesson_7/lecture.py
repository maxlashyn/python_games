""" exceptions """
""" Exception examples (syntax error, divide by zero etc) """
# 12/0 -> ZeroDivisionError
# for a as t ->SyntaxError:

""" catch exception """
""" single """
try:
    a = 12 / 0
except ZeroDivisionError:
    print('delenie na 0')

""" group """
try:
    a = 1
except (SyntaxError, ZeroDivisionError):
    print('exception')

""" else: """
try:
    a = 1
except ZeroDivisionError:
    print('zero division')
else:
    print('else')

""" finaly: """
try:
    a = 1/0
except ZeroDivisionError:
    print('zero division')
finally:
    print('finaly')

""" create exception class """

class MyException(Exception):
    pass

""" throw exception (raise) """

try:
    a = 1
    if a == 1:
        raise MyException()

    while True:
        pass
except MyException:
    print('my exception')


""" catch parent - child exceptions """
class MyNewException(MyException):
    pass


try:
    a = 1
    if a == 1:
        raise MyNewException()

    while True:
        pass
except MyNewException:
    print('my new exception')
except MyException:
    print('my exception')
except Exception:
    print('exception')

""" get exceptions arguments """

try:
    a = 'error value'
    if a != 1:
        raise MyNewException({'msg':'message about exception', 'value':a})

    while True:
        pass
except MyNewException as e:
    print(e)



