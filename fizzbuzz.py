# -*- coding: utf-8 -*-
""" FizzBuzz Module """


def fizz_buzz(numb):
    """ FizzBuzz algorithm.

    agrs:
        numb (int): The first parameter.

    Returns:
        string: Fizz if divisible by 3 or contain 3 in digits.
            Buzz if divisible by 5 or contain 5 in digits.
            FizzBuzz if divisible by 3 and 5.
    """
    if not numb % 15:
        return "FizzBuzz"
    if not numb % 3 or "3" in str(numb):
        return "Fizz"
    if not numb % 5 or "5" in str(numb):
        return "Buzz"

    return numb
