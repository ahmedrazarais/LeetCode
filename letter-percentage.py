# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

 

# Example 1:

# Input: s = "foobar", letter = "o"
# Output: 33
# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
# Example 2:

# Input: s = "jjjj", letter = "k"
# Output: 0
# Explanation:
# The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.

def percentageLetter(s,letter):

        # check if letter not present simply return 0
        if letter not in s:
           return 0

        #calculating length of string
        length=len(s)

        # iterate over string and check letter occurence
        total_count=0
        for char in s:
            if char==letter:
                total_count+=1

        # calculate percentage
        per=int(total_count/length*100)
        return per

print(percentageLetter("foobar","o"))
                

