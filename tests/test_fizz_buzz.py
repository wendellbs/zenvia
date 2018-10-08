# -*- coding: utf-8 -*-
import unittest
from modules.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_return_the_numb(self):
        """ Test non divisible numbers by 3 or 5 """
        numbs = [1, 2, 4, 22, 44, 89, 98]

        for numb in numbs:
            self.assertEqual(fizz_buzz(numb), numb)

    def test_return_fizz(self):
        """ Test the divisible numbers by 3 or contain 3 in digits """
        numbs = [3, 9, 35, 51, 81, 99]

        for numb in numbs:
            self.assertEqual(fizz_buzz(numb), "Fizz")

    def test_return_buzz(self):
        """ Test the divisible numbers by 5 or contain 5 in digits """
        numbs = [5, 10, 20, 65, 85, 95]

        for numb in numbs:
            self.assertEqual(fizz_buzz(numb), "Buzz")

    def test_return_fizzbuzz(self):
        """ Test the divisible numbers by 3 and 5 simultaneously """
        numbs = [15, 30, 45, 60, 75, 90]

        for numb in numbs:
            self.assertEqual(fizz_buzz(numb), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
