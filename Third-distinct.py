def thirdMax( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct_max = set(nums)
        if len(distinct_max) < 3:
            return max(distinct_max)
        else:
            return sorted(distinct_max)[-3]
        

print(thirdMax([1,2,3]))