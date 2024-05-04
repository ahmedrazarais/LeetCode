# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

 

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.



def sortPeople(names,heights):
        # make copy list of orignal 
        copy_height=heights[:]
        # make in descending order
        copy_height.sort(reverse=True)
        # initail empty to store result
        person=[]

        # iterte therough copy list
        for i in copy_height:
            # check if number in copy also in orignal
            if i in heights:
                # if number found in orignal we get index at which it existsv in origanl listr
                index=heights.index(i)
                # we get value of names from names lst on that index
                value=names[index]
                # append the value in final list
                person.append(value)

        # return final output
        return person
                
print(sortPeople(["Alice","Bob","Bob"],[155,185,150]))