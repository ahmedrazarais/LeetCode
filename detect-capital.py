def detectCapitalUse(word):
    if word.isupper():  # Case 1: All letters are uppercase
        return True
    elif word.islower():  # Case 2: All letters are lowercase
        return True
    elif word[0].isupper() and word[1:].islower():  # Case 3: First letter is uppercase, others are lowercase
        return True
    else:
        return False


print(detectCapitalUse("USA"))  # True
print(detectCapitalUse("leetcode"))  # True
print(detectCapitalUse("Google"))  # True
print(detectCapitalUse("FlaG"))  # False
