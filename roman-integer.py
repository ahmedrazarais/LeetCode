
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
         # Dictionary to store integer values corresponding to Roman numerals
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        # Variable to store the total integer value
        total = 0
        
        # Variable to store the previous numeral's integer value
        prev_value = 0
        
        # Iterate over each character in the Roman numeral string
        for num in s:
            # Get the integer value of the current numeral
            value = dic[num]

            # Check if the current numeral's value is greater than the previous numeral's value
            if value > prev_value:               
                total += value - 2 * prev_value
            else:
                total += value
            
            # Update the previous numeral's value for the next iteration
            prev_value = value
        
        # Return the total integer value of the Roman numeral string
        return total

result=romanToInt("MCMXCIV")
print(result)