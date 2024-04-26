def luckyNumbers (matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky_numbers = []

        # Iterate over each row in the matrix
        for row_index, row in enumerate(matrix):
            # Find the minimum element in the current row
            min_in_row = min(row)
            # Find the index of the minimum element in the current row
            min_index = row.index(min_in_row)
            
            # Check if the minimum element in the row is also the maximum in its column
            if all(matrix[i][min_index] <= min_in_row for i in range(len(matrix))):
                lucky_numbers.append(min_in_row)

        return lucky_numbers
print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))