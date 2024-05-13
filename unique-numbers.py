# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


def uniqueOccurrences(arr):
        # initail dictionary to store count
        num_count={}
        for i in arr:
            num_count[i]=num_count.get(i,0)+1

         # Get the values from the dictionary
        values = list(num_count.values())
        
        # Check if the number of values is equal to the number of unique values
        return len(values) == len(set(values))
        


        
print(uniqueOccurrences([1,2]))