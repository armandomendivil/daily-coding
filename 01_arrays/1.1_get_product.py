# Get product of all other elements

# input: [1, 2, 3, 4, 5]
# output: [120, 60, 40, 30, 24]

# Easy solution

def _products(nums):
    output = []
    result = 1

    for num in nums:
        result = result * num

    for num in nums:
        output.append(int(result / num))

    return output

# what if you can't use division

def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)

    suffix_products = list(reversed(suffix_products))

    # Generate result from the product of prefixes and suffixes
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(
                prefix_products[i -1] * suffix_products[i + 1]
            )
    return result

input = [1, 2, 3, 4, 5]
# Easy way using division
print(
    _products(input)   
)

# Hard way using prefix and suffix technique
print(
    products(input)   
)