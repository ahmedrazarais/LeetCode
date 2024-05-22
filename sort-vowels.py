# Given a 0-indexed string s, permute s to get a new string t such that:

# All consonants remain in their original places. More formally, if there is an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i] = s[i].
# The vowels must be sorted in the nondecreasing order of their ASCII values. More formally, for pairs of indices i, j with 0 <= i < j < s.length such that s[i] and s[j] are vowels, then t[i] must not have a higher ASCII value than t[j].
# Return the resulting string.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.


def sortVowels(s):
           # Define vowels both lowercase and uppercase
            vowels = set("aeiouAEIOU")
            
             #Extract vowels
            extracted_vowels = [char for char in s if char in vowels]
            
            # Sort the extracted vowels
            sorted_vowels = sorted(extracted_vowels)
            
            #  Reconstruct the string
            result = []
            vowel_index = 0
            
            for char in s:
                if char in vowels:
                    result.append(sorted_vowels[vowel_index])
                    vowel_index += 1
                else:
                    result.append(char)
            
            # Convert list back to string and return
            return ''.join(result)