# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.



def find_disjoint(nums1, nums2):
    # for removing duplicates and list top again typeacst to list
        set_nums1=list(set(nums1))
        set_nums2=list(set(nums2))

        # iterate over filterded list and check conditions
        answer1=[i for i in set_nums1 if i not in set_nums2]
        answer2=[i for i in set_nums2 if i not in set_nums1]

        # append in big list
        answer=[answer1,answer2]


        return answer
   
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = find_disjoint(nums1, nums2)
print(result)  