def extend_list(nums):
    length = len(nums)
    count = 0
    for i in nums:
        if count == length:
            break
        nums.append(i)
        count += 1
    return nums

nums = [1, 3, 2, 1]
extended_nums = extend_list(nums)
print(extended_nums)
