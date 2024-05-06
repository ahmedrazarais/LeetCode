# t is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Note: The boy can buy the ice cream bars in any order.

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# You must solve the problem by counting sort.


def maxIceCream(costs,coins):
        
        costs.sort()    # sort arrayu in ascending array

        # check is f in sorted array list index 0 is greater than coins 
        if costs[0]>coins:
            return 0

        total=0   # to store sum result
        count=0   # to store iteerations count

        # iterate over list
        for i in costs:
             # Check if adding the current cost exceeds the available coins
            if total + i <= coins:
                total+=i
                count+=1
            else:
                break   # if coins are less and cost exceeds
        return count

print(maxIceCream([1,2,3,4,5],9))

                