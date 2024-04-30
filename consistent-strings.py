def count_consistent_strings(allowed, words):
    count = 0
    for word in words:
        is_consistent = True
        for char in word:
            if char not in allowed:
                is_consistent = False
                break
        if is_consistent:
            count += 1
    return count


allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(count_consistent_strings(allowed, words))
