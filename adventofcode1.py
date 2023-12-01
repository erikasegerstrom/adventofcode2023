import re

valid_char_digits_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

sum_pt_1 = 0
sum_pt_2 = 0

def find_digit(row) -> int:
    """
    Find first and last int in string, return concatenated digit
    """
    split_row = [n for n in row]
    split_row_digits = [n for n in split_row if n.isdigit()]
    first_digit = split_row_digits[0]
    last_digit = split_row_digits[len(split_row_digits)-1]
    digit = int(str(first_digit) + str(last_digit))

    return digit

def find_digit_pt_2(row, valid_dict) -> int:
    """
    Find first and last key or value from valid_char_digits_dict in string, return concatenated digit
    """
    content_dict = {}
    for key, value in valid_dict.items():
        """ Find index of string occurances, include overlaps """
        indices_1 = [m.start() for m in re.finditer(key, row)]
        """ Find index of int occurances """
        indices_2 = [i for i, x in enumerate(row) if x == str(value)]

        for index in indices_1:
            content_dict[index] = value
        for index in indices_2:
            content_dict[index] = value
                
    digit = int(str(content_dict[min(content_dict)]) + str(content_dict[max(content_dict)]))

    return digit

with open('inputs/day1.txt') as f:
    raw = f.read().splitlines()

    for row in raw:
        """ Part 1 """
        sum_pt_1 += find_digit(row)

        """ Part 2 """
        sum_pt_2 += find_digit_pt_2(row, valid_char_digits_dict)

print("Sum part 1: ", sum_pt_1)
print("Sum part 2: ", sum_pt_2)