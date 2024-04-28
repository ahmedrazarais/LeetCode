# A self-dividing number is a number that is divisible by every digit it contains.


# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

def self_dividing_numbers(left, right):
    result = []
    for num in range(left, right + 1):
        num_str = str(num)
        if '0' not in num_str and all(num % int(digit) == 0 for digit in num_str):
            result.append(num)
    return result

# Test cases
left1, right1 = 1, 22
left2, right2 = 47, 85

print(self_dividing_numbers(left1, right1))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
print(self_dividing_numbers(left2, right2))  # Output: [48, 55, 66, 77]
