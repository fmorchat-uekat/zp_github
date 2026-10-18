def list_even(numbers):
    for number in numbers:
        if(number % 2 == 0):
            print(number)

numbers = range(10)
list_even(numbers)