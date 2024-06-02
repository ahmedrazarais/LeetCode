# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.



def minSetSize(arr):
                
        arr_dic = {}
        length_org_arr = len(arr)

        # Count the frequency of each number in the array
        for num in arr:
            arr_dic[num] = arr_dic.get(num, 0) + 1

        # Convert the frequencies into a list and sort in descending order
        frequencies = sorted(arr_dic.values(), reverse=True)

        count = 0
        removed_elements = 0

        # Remove numbers until at least half of the array is removed
        for freq in frequencies:
            removed_elements += freq
            count += 1
            if removed_elements >= length_org_arr // 2:
                break

        return count

print(minSetSize([3,3,3,3,5,5,5,2,2,7]))