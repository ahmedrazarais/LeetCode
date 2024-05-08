# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.


def findMedianSortedArrays(nums1,nums2):
        
        # Combine the lists and sort them
        num = nums1 + nums2
        num.sort()

        if len(num) % 2 != 0:
            # If the length of num is odd
            for_odd = len(num) // 2
            odd_answer = num[for_odd]
            return odd_answer
        else:
            # If the length of num is even
            for_even_first_index = len(num) // 2 - 1
            for_even_second_index = len(num) // 2
            median = (num[for_even_first_index] + num[for_even_second_index]) / 2
            return median
        
print(findMedianSortedArrays([1,2],[3]))
                


