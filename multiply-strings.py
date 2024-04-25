def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        number=[]
        number.append(num1)
        number.append(num2)
        number=[int(i) for i in number]
        result=1
        for i in number:
            result*=i

        result=str(result)
        return result

print(multiply("2","3"))