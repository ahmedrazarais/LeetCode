# You are given an integer array nums where the largest integer is unique.

# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 
def dominantIndex(nums):
        if len(nums) == 0:
          return -1
    
        # Step 1: Find the maximum value and its index
        max_value = max(nums)
        max_index = nums.index(max_value)
        
        # Step 2: Verify the condition
        for i, num in enumerate(nums):
            if i != max_index and max_value < 2 * num:
                return -1
        
        return max_index
            