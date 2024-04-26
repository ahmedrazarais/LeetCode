def rotate( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Calculate the effective rotation (in case k > len(nums))
        k %= len(nums)
        
        # Reverse the entire list
        nums.reverse()
        
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])

        return nums

print(rotate([1,2,3,4,5,6,7],3))