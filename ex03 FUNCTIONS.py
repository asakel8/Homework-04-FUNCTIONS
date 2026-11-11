def count_digits(s):
    count = 0

    for character in s:
        if character.isdigit():
            count = count + 1

    return count


print(count_digits('abc3ui6bc8p'))  