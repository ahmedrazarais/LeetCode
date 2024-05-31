
# A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

# Return the minimum cost to fly every person to a city such that exactly n people arrive in each city



def twoCitySchedCost(costs):
            costs.sort(key=lambda x: x[0] - x[1])
    
            total_cost = 0
            n = len(costs) // 2
            
            # Send the first n people to city A and the rest to city B
            for i in range(n):
                total_cost += costs[i][0]
            for i in range(n, 2 * n):
                total_cost += costs[i][1]
            
            return total_cost
                

print(twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))