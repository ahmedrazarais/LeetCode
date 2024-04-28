# Given two positive integers a and b, return the number of common factors of a and b.

# An integer x is a common factor of a and b if x divides both a and b.

a = 12
b = 6
# find maximum from both number to apply loop
maximum_num=max(a,b)
# initial count 0 
count=0
for i in range (1,maximum_num+1):
    # check condition if both divisible
    if a%1==0 and b%i==0:
        # increment count
        count+=1

print(count)