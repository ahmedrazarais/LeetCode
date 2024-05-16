# 2442. Count Number of Distinct Integers After Reverse Operations

# You are given an array nums consisting of positive integers.

# You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.

# Return the number of distinct integers in the final array.


def countDistinctIntegers(nums):
        main=[]
        # type cast all elements of list to string first
        nums_str=[str(i) for i in nums]

        # now oppose every element and typecast it back to integer
        nums_reverse=[int(i[::-1]) for i in nums_str]
        
        # typecast orignal list to integer back
        nums_int=[int(i) for i in nums]


        main=set(nums_int+nums_reverse)

        return len(main) 

print(countDistinctIntegers([1,22,31,4]))