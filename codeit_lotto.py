from random import randint

def generate_numbers():
    num_list = []
    while len(num_list) != 6:
        num = randint(1, 45)
        if num in num_list:
            continue
        else:
            num_list.append(num)
    num_list.sort()
    return num_list


def draw_winning_numbers():
    bonus_num_list = []
    bonus_num_list = generate_numbers()
    bonus_num = randint(1, 45)
    if bonus_num not in bonus_num_list:
        bonus_num_list.append(bonus_num)
    return bonus_num_list

list1 = generate_numbers()
list2 = draw_winning_numbers()
print(list1)
print(list2)

def count_matching_numbers(list1, list2):
    count = 0
    for i in range(0, len(list1)):
        if list1[i] in list2:
            count += 1
    return count

def check(numbers, winning_numbers):
    same_number = count_matching_numbers(numbers, winning_numbers)
    if same_number == 6:
        return 1000000000
    elif same_number == 5:
        if winning_numbers[6] in numbers:
            return 50000000
        else:
            return 1000000
    elif same_number == 4:
        return 50000
    elif same_number == 3:
        return 5000
    else:
        return 0

print(check(list1, list2))
