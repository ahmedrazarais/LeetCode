def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    # Create dictionaries to store character frequencies
    s_freq = {}
    t_freq = {}
    
    # Populate frequency dictionaries for both strings
    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1
        
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
    
    # Check if the dictionaries are equal
    return s_freq == t_freq


s1 = "anagram"
t1 = "nagaram"
print(isAnagram(s1, t1)) 

s2 = "rat"
t2 = "car"
print(isAnagram(s2, t2))  

    

