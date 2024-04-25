def find_needle(haystack, needle):
    # find will give first index
    index = haystack.find(needle)
    if index == -1:     # is not found
        return -1
    else:
        return index

# Test cases
haystack = "razabutsad"
needle = "sad"
print(find_needle(haystack, needle))
