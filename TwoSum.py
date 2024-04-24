def twoSum(nums, target):
        
        # initializing empty dictionary
        # elemts are keys and indices are value
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return []  # If no solution is found

# checking output
result=twoSum([1,2,3,4,5],8)
print(result)
