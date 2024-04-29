grid = [[1,3],[2,2]]
grad = []
output = []

# Extract numbers from the grid
for row in grid:
    for num in row:
        grad.append(num)

# Find the repeating number
repeating_num = None
for num in grad:
    if grad.count(num) == 2:
        repeating_num = num
        break

# Calculate length of the list
length = len(grad)

# Calculate the actual sum of the numbers in the list
actual_sum = sum(grad)

# Calculate the sum of numbers from 1 to n^2
sum_n = (length * (length + 1)) // 2

# Find the missing number
missing_num = sum_n - actual_sum + repeating_num

output.append(repeating_num)
output.append(missing_num)
print(output)
