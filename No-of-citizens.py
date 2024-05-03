# You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

# The first ten characters consist of the phone number of passengers.
# The next character denotes the gender of the person.
# The following two characters are used to indicate the age of the person.
# The last two characters determine the seat allotted to that person.
# Return the number of passengers who are strictly more than 60 years old.

 

# Example 1:

# Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2
# Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.
# Example 2:



def countSeniors(details):
        # initial empty list
        citizens=[]
        citizen_count=0
        # iterate through list
        for get in details:
            citizens.append(get[11:13])
        
        #typecast list elements to integer
        citizens=[int(i) for i in citizens]

        # check citizen with age greater than 60
        for i in citizens:
            if i>60:
                citizen_count+=1

        return citizen_count

print(countSeniors( ["7868190130M7522","5303914400F9211","9273338290F4010"]))

        