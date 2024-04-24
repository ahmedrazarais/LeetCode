# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

def lengthOfLastWord(s):
        s=s.strip().split()   # strip to remove whitespaces and split to malke list
        s.reverse() # reverse the entire list
        return len(s[0]) # returning first index length after reverse

result=lengthOfLastWord("luffy is still joyboy")
print(result)