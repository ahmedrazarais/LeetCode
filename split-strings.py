# Given an array of strings words and a character separator, split each string in words by separator.

# Return an array of strings containing the new strings formed after the splits, excluding empty strings.

# Notes

# separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
# A split may result in more than two strings.
# The resulting strings must maintain the same order as they were initially given.



def splitWordsBySeparator(words,separator):
       
        # Initialize an empty list to store the split words
        split_words = []

        # Iterate over each string in the list
        for string in words:
            # Split the string using the separator and extend the split_words list
            split_words.extend(string.split(separator))

          # Exclude empty strings from the list
        split_words = [word for word in split_words if word != ""]
        
        # Return the result
        return split_words
                
print(splitWordsBySeparator( ["one.two.three","four.five","six"],"."))