# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

# The words in paragraph are case-insensitive and the answer should be returned in lowercase.


def mostCommonWord(paragraph,banned):
           
        # Convert paragraph to lowercase
        paragraph = paragraph.lower()
        
        # Split paragraph into words without punctuation
        words = []
        word = ""
        for char in paragraph:
            if char.isalnum():  # Check if character is alphanumeric
                word += char
            elif word:  # If word is not empty, add it to the list of words
                words.append(word)
                word = ""
        
        # Add the last word if it's not empty
        if word:
            words.append(word)
        
        # Filter out banned words
        words = [word for word in words if word not in banned]
        
        # Dictionary to store word frequencies
        word_freq = {}
        
        # Count word frequencies
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Find the most frequent word that is not banned
        max_freq = 0
        most_common_word = ""
        for word, freq in word_freq.items():
            if freq > max_freq:
                max_freq = freq
                most_common_word = word
        
        return most_common_word

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))