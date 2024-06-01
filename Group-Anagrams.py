# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


def groupAnagrams(strs):
         # Create an empty dictionary to hold the groups of anagrams
        anagrams = {}

        # Iterate over each word in the input list
        for word in strs:
            # Sort the characters of the word to form the key
            sorted_word = ''.join(sorted(word))

            # If the sorted_word is not already a key in the dictionary,
            # add it with an empty list as its value
            if sorted_word not in anagrams:
                anagrams[sorted_word] = []

            # Append the current word to the list corresponding to the sorted_word key
            anagrams[sorted_word].append(word)

        # Convert the values of the dictionary (which are lists of anagrams) to a list
        # and return it
        return list(anagrams.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) 