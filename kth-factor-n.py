def kth_factor(n, k):
    # Initialize an empty list to store factors
    factors = []
    
    # Find all factors of n
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    # Sort the list of factors in ascending order
    factors.sort()
    
    # Check if the list of factors has at least k elements
    if len(factors) >= k:
        # Return the kth factor
        return factors[k - 1]
    else:
        # Return -1 to indicate that n has fewer than k factors
        return -1


n = 12
k = 3
print(kth_factor(n, k))  # Output: 3

