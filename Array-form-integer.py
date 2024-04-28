def addToArrayForm(num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        # convert all elements to string
        num=[str(i) for i in num]
        # .join to concatecate in singli string
        num="".join(num)
        # calculate result
        result=k+int(num)
        # copnvert result to string
        result=str(result)
        # convert the string to list
        result=list(result)
        # after that finally typecast to integre
        final_result=[int(i) for i in result]

        return final_result

print(addToArrayForm([1,2,0,0],34))