class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums=nums
        self.target=target
        for i in self.nums:
            if i==self.target:
                return(self.nums.index(i))
        else:
            self.nums.append(self.target)
            self.nums.sort()
            return(self.nums.index(self.target))

s=Solution()
print(s.searchInsert([1,3,4,5],4))