def multi_for(numbers):
    numbers_multiplied = []
    for number in numbers:
        numbers_multiplied.append(number * 2)
    return numbers_multiplied

def multi_list(numbers):
    numbers_multiplied = [number * 2 for number in numbers]
    return numbers_multiplied

numbers = [2,84,91,0,74]
numbers_mult_for = multi_for(numbers)
numbers_mult_list = multi_list(numbers)

for number in numbers_mult_for:
    print(number)
for number in numbers_mult_list:
    print(number)
