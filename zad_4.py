def list_every_other(numbers):
    i = 0
    for number in numbers:
        i = i + 1
        if i % 2 == 0:
            print(number)

numbers = range(10)
list_every_other(numbers)