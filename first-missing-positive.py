# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.


def fisrtmissing(nums):
    # convert list to set first to remove duplicaytes also for faster look
    nums=set(nums)
    
    # start with first positive number
    i=1

    while i in nums:
        i+=1   # move to next if i found
    
    return i    # if number not found then return that number

print(fisrtmissing([1,3,4,5]))
