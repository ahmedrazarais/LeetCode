def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # To store every number frequency
        nums_frequency={}

        for i in nums:
            nums_frequency[i]=nums.count(i)

        for key,value in nums_frequency.items():
            if value==1:
                return key
            
print(singleNumber([1,2,3,1,2,3,31]))