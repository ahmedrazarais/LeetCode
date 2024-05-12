# You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.

# Return an array that consists of indices of peaks in the given array in any order.

# Notes:

# A peak is defined as an element that is strictly greater than its neighboring elements.
# The first and last elements of the array are not a peak.



def findPeaks(mountain):
        peaks=[]   # initali empty to store induices
        # loop through loength of list but start from 2nd element till second last
        for i in range(1,len(mountain)-1):
            # checking peak condition
            if mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]:
                # append in list
                peaks.append(i)

        return peaks

print(findPeaks([1,2,3,4,5]))