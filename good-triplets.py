# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.

# Return the number of good triplets.

 

# Example 1:

# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
# Example 2:

# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.



def countGoodTriplets(arr,a,b,c):
    # Initialize the count of good triplets to 0
    triplets_count = 0
    
    # Loop through all possible combinations of three elements in the array
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                # Check if the conditions for a good triplet are met
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    # If the conditions are met, increment the count of good triplets
                    triplets_count += 1

    # Return the final count of good triplets
    return triplets_count

# Test case
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))  # Output should be 4
