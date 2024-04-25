
def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()    # lower case
        # use list comprehension include only alpha numeric values
        s = [i for i in s if i.isalnum()]
        # use .join
        word = "".join(s)
        # Checking for palindrome
        if word[:] == word[::-1]:
            return True
        # If not palindrome
        else:
            return False   # removed "checking palindrome"
result=isPalindrome("A man , A plan # A CAnal : Panama")
print(result)
