# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def addUp(nums, k):
    set_nums = set()
    for n in nums:
        set_nums.add(abs(n - k))
        if n in set_nums:
            return True

    return False

assert addUp([10, 15, 3, 7], 17)
assert addUp([10, 15, 3, 7], 18)
assert not addUp([10, 15, 3, 7], 19)