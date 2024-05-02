def optimalDivision(nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # typeacst list elements to string 
        nums=[str(i) for i in nums]

        # if len is 1 so simply return that number
        if len(nums)==1:
            return nums[0]
        
        #if len is 2 so just return withoout parenthesis
        if len(nums)==2:
            result=nums[0] + "/" + nums[1]
            return result
        
        # initial it as empty
        ope=""
        ope+=nums[0]+"/"+"("

        for i in nums[1:-1]:  # Iterate over elements except the first and last
            ope += i + "/"

        ope += nums[-1] + ")"  # Add the last element with ")"
        return ope
                
print(optimalDivision([1000,100,10,2]))