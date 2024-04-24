class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count occurrences of characters in ransomNote and magazine
        ransom_counts = {}
        magazine_counts = {}
        
        for char in ransomNote:
            ransom_counts[char] = ransom_counts.get(char, 0) + 1
        
        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1
        
        # Check if magazine has enough characters to satisfy ransomNote
        for char, count in ransom_counts.items():
            if char not in magazine_counts or magazine_counts[char] < count:
                return False
        
        return True

s = Solution()
result = s.canConstruct("aa", "aab")
print(result)
