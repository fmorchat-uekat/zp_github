import string


def is_palindrome(text: str) -> bool:
    text = text.lower()
    text = "".join(text.split())
    i, j = 0, len(text) - 1

    while i < j:
        if text[i] != text[j]:
            return 0
        i = i + 1
        j = j - 1
    return 1


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        i = 2
        res = 0
        a, b = 0, 1
        while i <= n:
            res = a + b
            a = b
            b = res
            i = i + 1
        return res


def count_vowels(text: str) -> int:
    i, j = 0, len(text)
    res = 0
    text = text.lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'ó', 'ą', 'ę']
    while i < j:
        if text[i] in vowels:
            res = res + 1
        i = i + 1
    return res


def calculate_discount(price: float, discount: float) -> float:
    if discount > 1 or discount < 0:
        return ValueError
    return price - (price * discount)


def flatten_list(nested_list: list) -> list:
    i, j = 0, len(nested_list)
    end_list = []
    while i < j:
        if type(nested_list[i]) is not list:
            end_list.append(nested_list[i])
        else:
            temp_list = flatten_list(nested_list[i])
            k, h = 0, len(temp_list)
            while k < h:
                end_list.append(temp_list[k])
                k = k + 1
        i = i + 1
    return end_list


def word_frequencies(text: str) -> dict:
    words = text.lower().split()
    end_dict = {}
    translator = str.maketrans('', '', string.punctuation)
    for word in words:
        word = word.translate(translator)
        if word in end_dict:
            end_dict[word] = end_dict[word] + 1
        else:
            end_dict[word] = 1
    return end_dict


def is_prime(n: int) -> bool:
    if n < 2:
        return 0
    i = 2
    while i < n:
        if n % i == 0:
            return 0
        i = i + 1
    return 1
