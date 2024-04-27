def searchMatrix(matrix, target):
    for lists in matrix:
        for numbers in lists:
            if numbers == target:
                return True
    return False

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(searchMatrix(matrix, target))
