# This problem was asked by Slack.

# You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

# For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

# Given this string, return the original integers in sorted order. In the example above, this would be 357.

WORD_MAP = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

def get_char_count_dict(string):
    letter_dict = dict()

    for char in string:
        if char not in letter_dict:
            letter_dict[char] = 0
        letter_dict[char] += 1
    
    return letter_dict

def use_digit(letter_dict, word_dict, digit):
    for char in word_dict:
        # print(word_dict.get(letter_dict))
        if char not in letter_dict or word_dict[char] > letter_dict[char]:
            return letter_dict, 0
    
    for char in word_dict:
        letter_dict[char] -= word_dict[char]
    
    letter_dict, uses = use_digit(letter_dict, word_dict, digit)
    return letter_dict, uses + 1

def get_sorted_nums(string):
    letter_dict = get_char_count_dict(string)

    result = 0
    for i in range(10):
        word = WORD_MAP[i]
        word_dict = get_char_count_dict(word)
        letter_dict, uses = use_digit(letter_dict, word_dict, i)

        while uses > 0:
            result = result * 10 + i
            uses -= 1
    
    return result

print(get_sorted_nums("niesevehrtfeev"))

# Tests
assert get_sorted_nums("niesevehrtfeev") == 357
