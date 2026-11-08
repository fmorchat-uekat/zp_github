import pytest
import zp_github.funcs as funcs


def test_pal():
    assert funcs.is_palindrome('kajak') == 1
    assert funcs.is_palindrome("Kobyła ma mały bok") == 1
    assert funcs.is_palindrome('python') == 0
    assert funcs.is_palindrome('') == 1
    assert funcs.is_palindrome('A') == 1


def test_fibonacci():
    assert funcs.fibonacci(0) == 0
    assert funcs.fibonacci(1) == 1
    assert funcs.fibonacci(5) == 5
    assert funcs.fibonacci(10) == 55
    assert funcs.fibonacci(-1) == 0


def test_vowels():
    assert funcs.count_vowels("Python") == 2
    assert funcs.count_vowels("AEIOUY") == 6
    assert funcs.count_vowels("bcd") == 0
    assert funcs.count_vowels("") == 0
    assert funcs.count_vowels("Test żółwia") == 4


def test_discount():
    assert funcs.calculate_discount(100, 0.2) == 80.0
    assert funcs.calculate_discount(50, 0) == 50.0
    assert funcs.calculate_discount(200, 1) == 0.0
    assert funcs.calculate_discount(100, -0.1) == ValueError
    assert funcs.calculate_discount(100, 1.5) == ValueError


def test_flatten():
    assert funcs.flatten_list([1, 2, 3]) == [1, 2, 3]
    assert funcs.flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert funcs.flatten_list([]) == []
    assert funcs.flatten_list([[[1]]]) == [1]
    assert funcs.flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


def test_freq():
    assert funcs.word_frequencies("To be or not to be") == {"to": 2, "be": 2, "or": 1, "not": 1}
    assert funcs.word_frequencies("Hello, hello!") == {"hello": 2}
    assert funcs.word_frequencies("") == {}
    assert funcs.word_frequencies("Python Python python") == {"python": 3}
    assert funcs.word_frequencies("Ala ma kota, a kot ma ale") == {'a': 1, 'ala': 1, 'ale': 1, 'kot': 1, 'kota': 1, 'ma': 2}


def test_prime():
    assert funcs.is_prime(2) == 1
    assert funcs.is_prime(3) == 1
    assert funcs.is_prime(4) == 0
    assert funcs.is_prime(0) == 0
    assert funcs.is_prime(1) == 0
    assert funcs.is_prime(5) == 1
    assert funcs.is_prime(97) == 1