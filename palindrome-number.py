def isPalindrome(x):
       
        # Check if x is negative or ends with a 0 (excluding 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        original_x = x
        
        while x > 0:
            # Extract the last digit
            digit = x % 10
            # Build the reversed number
            reversed_num = reversed_num * 10 + digit
            # Move to the next digit
            x //= 10
        
        # Check if the original number is equal to its reversed version
        return original_x == reversed_num

result=isPalindrome(110)
print(result)