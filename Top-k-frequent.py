# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]




def topKFrequent(nums,k):
        freq={}     # to store numbers frequency
        numbers=[] # to store frequent numbers till k

        # iterate over list to make dictionary
        for i in nums:
            # key is numbers and its count is value
            freq[i]=freq.get(i,0)+1

        # range till k 
        for _ in range (k):
                # calculate max value from dictionaries keys
                max_val=max(freq.values())
                # iterate over dictionary items 
                for key,value in freq.items():
                        # iof value == max value
                        if value==max_val:
                            # append in list
                            numbers.append(key)
                            del freq[key]   # remove max key value   
                            break  # break ott loop when k meets


        return numbers   


print(topKFrequent([1,1,1,2,2,3],2))