def longestCommonPrefix(strs):
    # If the input array is empty, return an empty string
    if not strs:
        return ""
    
    # Iterate through the characters of the first string
    for i, char in enumerate(strs[0]):
        # Check if the character is present in the same position in all strings
        for string in strs[1:]:
            # If the current index is out of range for the current string or
            # the character does not match, return the substring up to the current index
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    
    # If no mismatches were found, return the first string
    return strs[0]

# Test cases
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs1))  
print(longestCommonPrefix(strs2))  
