# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

# Return a list of groups such that each person i is in a group of size groupSizes[i].

# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.



def groupThePeople(groupSizes):
         # Dictionary to collect people by their group sizes
        size_to_people = {}
        
        # Populate the dictionary
        for person, size in enumerate(groupSizes):
            if size not in size_to_people:
                size_to_people[size] = []
            size_to_people[size].append(person)
        
        result = []

        # Create the groups based on collected people
        for size, people in size_to_people.items():
            for i in range(0, len(people), size):
                result.append(people[i:i + size])
        
        return result
            


print(groupThePeople([3,3,3,3,3,1,3]))