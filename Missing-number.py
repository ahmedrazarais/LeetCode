# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.



def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # fist clculate length of list
        length=len(nums)

        # calculate sum of list
        sum_list=sum(nums)

        # By formula # calculate sum from 0 to n

        sum_n=(length * (length + 1)) / 2

        # for missing number'

        missing_no=int(sum_n-sum_list)
        return missing_no

print(missingNumber(nums = [3,0,1]))