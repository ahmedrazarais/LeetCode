# You are given a 1-indexed integer array nums of length n.

# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

# Return the sum of the squares of all special elements of nums.



def sumOfSquares(nums):
        squares = []  # Initialize empty list to store elements that fulfill conditions
        
        length = len(nums)  # Length of the list

        # Iterate over indices of nums
        for num in range(1, length + 1):
            # Skip if num is zero to avoid division by zero error
            if num == 0:
                continue
            
            # Check if num divides length evenly
            if length % num == 0:
                squares.append(nums[num - 1] ** 2)  # Append square of nums[num - 1] to squares
        
        total = sum(squares)  # Calculate the sum of squares
        return total  # Return the total sum


print(sumOfSquares([1,2,3,4]))