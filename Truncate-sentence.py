
def truncateSentence( s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.strip().split()
        result = ""
        count = 0
        for i in s:
            if count == k:
                break
            result += i
            result += " "
            count += 1
        return result.strip()  # Remove trailing space
    


print(truncateSentence("Hello how are you Contestant", 4))