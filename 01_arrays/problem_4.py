# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def positive_numbers(nums):
    min = 100000
    max = -100000

    sum = 0;

    for num in nums:
      if num > 0:
        if num < min:
          min = num
        if num > max:
          max = num

        sum = sum + num

    return sum, max

def fn(nums):
  sum, max = positive_numbers(nums)

  expected = max * (max + 1) / 2
  result = 0

  if expected == sum:
    result = max + 1
  else:
    result = expected - sum

  return result

assert fn([3, 4, -1, 1]) == 2
assert fn([1, 2, 0]) == 3
