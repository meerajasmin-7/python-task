# 1. Alternating Digit Sum

# def alternate_digit_sum(n):
#     digits = str(n)
#     total = 0

#     for i in range(len(digits)):
#         if i % 2 == 0:
#             total += int(digits[i])
#         else:
#             total -= int(digits[i])

#     return total

# # Example
# n = 521
# print(alternate_digit_sum(n))

# 2. Separate the Digits in an Array

# def separate_digits(nums):
#     result = []

#     for num in nums:
#         for digit in str(num):
#             result.append(int(digit))

#     return result

# # Example
# nums = [13, 25, 83, 77]
# print(separate_digits(nums))

# List Comprehension Version:

nums = [13, 25, 83, 77]

result = [int(digit) for num in nums for digit in str(num)]

print(result)