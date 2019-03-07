from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 6:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)
    return sorted(numbers)

def draw_winning_numbers():
    winning_numbers = generate_numbers()
    while len(winning_numbers) < 7:
        new_number = randint(1, 45)
        if new_number not in winning_numbers:
            winning_numbers.append(new_number)
    return winning_numbers

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count += 1
    return count

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0
