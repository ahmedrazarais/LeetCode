# Given a sentence text (A sentence is a string of space-separated words) in the following format:

# First letter is in upper case.
# Each word in text are separated by a single space.
# Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

# Return the new text following the format shown above.

 

def arrangeWords(text):
        text=text.lower().split()     # all lower and saplit to make list
        # to mstore result of new
        new_text=""
        # use sorted use key as len
        text=sorted(text,key=len)
        # capitalize first character first letter
        text[0]=text[0].capitalize()
        # iuterate over list
        for i in text:
            # concatecate into new string
            new_text+=i
            new_text+=" "

        return new_text.strip()
print(arrangeWords("is i am"))