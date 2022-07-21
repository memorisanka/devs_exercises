from functions.FizzBuzz import *


def test_if_number_is_divided_by_3_and_5():
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"
    assert fizz_buzz(90) == "FizzBuzz"


def test_if_number_is_divided_by_3():
    assert fizz_buzz(9) == "Fizz"
    assert fizz_buzz(21) == "Fizz"


def test_if_number_is_divided_by_5():
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(20) == "Buzz"


def test_if_number_is_not_divided_by_3_5():
    assert fizz_buzz(28) == 0
    assert fizz_buzz(43) == 0
