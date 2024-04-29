# Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

# Return the selected integer.

 

# Example 1:

# Input: nums = [3,2,1,4]
# Output: 2
# Explanation: In this example, the minimum value is 1 and the maximum value is 4. Therefore, either 2 or 3 can be valid answers.
# Example 2:

# Input: nums = [1,2]
# Output: -1
# Explanation: Since there is no number in nums that is neither the maximum nor the minimum, we cannot select a number that satisfies the given condition. Therefore, there is no answer.


def findNonMinOrMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum_no=max(nums)
        minimum_no=min(nums)
        nums=[i for i in nums if i!=maximum_no and i!=minimum_no]
        if len(nums)==0:
            return -1
        else:

            return (nums[0])
        
print(findNonMinOrMax([1,2,3,4]))