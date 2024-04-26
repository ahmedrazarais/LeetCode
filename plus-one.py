def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[str(i) for i in digits]
        digits=int("".join(digits))

        digits+=1
        digits=str(digits)

        digits=list(digits)
        digits=[int(i) for i in digits]

        return digits

print(plusOne([1,3,4]))
                