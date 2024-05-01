def kth_smallest(matrix, k):
    # Flatten the matrix into a 1D list
    flattened_matrix = [element for row in matrix for element in row]

    # Sort the flattened list
    flattened_matrix.sort()

    # Return the kth smallest element
    return flattened_matrix[k-1]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(kth_smallest(matrix, k))
