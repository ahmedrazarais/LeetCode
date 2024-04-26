
def numberOfSpecialChars(word):
        """
        :type word: str
        :rtype: int
        """
        lower_chars=[]  # for holding lowercase
        upper_chars=[]      # fore holding upper case
        total_count=0   # to put total count
        for char in word:
            if char == char.lower():
                lower_chars.append(char)


            if char == char.upper():
                char=char.lower()
                upper_chars.append(char)

        
        # use set and list to remove dupliactesa and after again getting list
        lower_chars=list(set(lower_chars))
        upper_chars=list(set(upper_chars))

        for char in lower_chars:
            if char in upper_chars:
                total_count+=1



        return total_count

print(numberOfSpecialChars("abc"))
        