# Given a non-negative integer num, return true if num can be expressed as the sum of any non-negative integer and its reverse, or false otherwise.


def is_sum_of_integer_and_reverse(num):
    # Loop through all possible integers from 0 to num
    for i in range(num + 1):
        # Convert the current integer to a string
        i_str = str(i)
        
        # Reverse the string representation of the integer
        reverse_str = i_str[::-1]
        
        # Convert the reversed string back to an integer
        reverse_int = int(reverse_str)
        
        # Check if the sum of the integer and its reverse equals num
        if i + reverse_int == num:
            # If a valid pair is found, return True
            return True
    
    # If no valid pair is found after checking all possibilities, return False
    return False

# Example usage:
print(is_sum_of_integer_and_reverse(121))  
