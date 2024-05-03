# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1


def firstUniqChar(s):
       # Dictionar to store character frequencies
        char_freq = {}
        
        # Count the frequency of each character in the string
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        # Iterate over the string to find the first non-repeating character
        for i, char in enumerate(s):
            if char_freq[char] == 1:
                return i
        
        # If no non-repeating character is found, return -1
        return -1

print(firstUniqChar("leetcode"))