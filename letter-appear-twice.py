def first_duplicate_letter(s):
    seen = {}
    for i, char in enumerate(s):
        if char in seen:
            return char
        seen[char] = i
    return None

# Test cases
s1 = "abccbaacz"
s2 = "abcdd"

print(first_duplicate_letter(s1))  # Output: "c"
print(first_duplicate_letter(s2))  # Output: "d"
