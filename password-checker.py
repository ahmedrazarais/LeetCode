# A password is said to be strong if it satisfies all the following criteria:

# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.


def isStrongPassword(password):
        # Check if password has at least 8 characters
        if len(password) < 8:
            return False
        
        # Check if password contains at least one lowercase letter
        if not any(char.islower() for char in password):
            return False
        
        # Check if password contains at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False
        
        # Check if password contains at least one digit
        if not any(char.isdigit() for char in password):
            return False
        
        # Check if password contains at least one special character
        special_characters = "!@#$%^&*()-+"
        if not any(char in special_characters for char in password):
            return False
        
        # Check if password does not contain 2 of the same character in adjacent positions
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
        
        return True


print(isStrongPassword("IloveLe3tcode!"))
