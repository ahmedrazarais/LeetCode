def scoreOfString(s):
        """
        :type s: str
        :rtype: int
        """
        ascci_dic={'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}
        count=[]     # for getting values from string 
        output=[] # to get output

        # loop through string
        for i in s:
            # check in dictionary
            if i in ascci_dic:
                # appned in count list value iof that alphabet
                count.append(ascci_dic[i])
        # loop to perform task
        for i in range(len(count)-1):
            # use abse as mod
            result=abs(count[i]-count[i+1])
            # append in output list
            output.append(result)

        # calculate sum
        total=sum(output)
        return total

print(scoreOfString("hello"))
                