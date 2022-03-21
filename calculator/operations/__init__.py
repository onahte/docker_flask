""" These are the Operation Classes"""


class Addition:
    """ This is the addition class"""

    # this defines a static method that you can use without instantiating the calculator class
    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return value_1 + value_2


class Subtraction:
    """ This is the subtraction class"""

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the subtract method"""
        return value_1 - value_2


class Multiplication:
    """ This is the multiplication class"""

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the multiply method"""
        return value_1 * value_2

class Division:
    """ This is the division class"""

    @staticmethod
    def divide(value_1, value_2):
        """ This is the divide method"""
        return value_1 / value_2
