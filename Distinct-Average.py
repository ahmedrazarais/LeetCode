# 2465. Number of Distinct Averages
# Easy
# Topics
# Companies
# Hint
# You are given a 0-indexed integer array nums of even length.

# As long as nums is not empty, you must repetitively:

# Find the minimum number in nums and remove it.
# Find the maximum number in nums and remove it.
# Calculate the average of the two removed numbers.
# The average of two numbers a and b is (a + b) / 2.

# For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
# Return the number of distinct averages calculated using the above process.

# Note that when there is a tie for a minimum or maximum number, any can be removed.

def distinctAverages(nums):
    # sort array in ascending order
    nums.sort()

    # average list to store numbers
    average=[]

    # iterate till nums not empty
    while nums:
        # getting minium and maximum number ands remove it from list
        mini=nums.pop(0)
        maxi=nums.pop(-1)

        # calculating avg
        avg=(mini+maxi)/2
        # append in list
        average.append(avg)
    # convert in setr to remove duplicate
    res=set(average)
    # calculating len set
    res=len(res)
    
    return res   

