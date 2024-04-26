def fizzBuzz(n):
    # To hold elements in array
    array=[]

    # loop till given n
    for i in range (1,n+1):

        # Given condition
        if i%3==0 and i%5==0:
            array.append("FizzBuzz")
        

        elif i%3==0:
            array.append("Fizz")

        
        elif i%5==0:
            array.append("Buzz")


        else:
            array.append(str(i))


    return array

print(fizzBuzz(15))