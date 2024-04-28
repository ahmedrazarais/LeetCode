def countDigits( num):
        """
        :type num: int
        :rtype: int
        """
        # convert it to string
        num_string=str(num)
        # make list of digits
        num_string=list(num_string)

        # typecast back to integer
        num_int=[int(i) for i in num_string]
        
        #initial count =0
        divide_count=0
       
        # check divide condition
        for i in num_int:
            if num%i==0:
                divide_count+=1
        
        return divide_count

print(countDigits(123))