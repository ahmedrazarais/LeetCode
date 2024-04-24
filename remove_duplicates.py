def removeDuplicates(nums):
    # Check if nums is empty
    if not nums:
        return 0
    
    # Initialize the pointer to track the end of unique elements
    unique_end = 0
    
    # Iterate through the array starting from the second element
    for current in range(1, len(nums)):
        # If the current element is different from the previous unique element,
        # it's a new unique element
        if nums[current] != nums[unique_end]:
            # Move the unique_end pointer forward
            unique_end += 1
            # Update nums[unique_end] with the new unique element
            nums[unique_end] = nums[current]
    
    # The count of unique elements is unique_end + 1
    return unique_end + 1

# Test the function
result = removeDuplicates([1, 1, 2])
print(result)
