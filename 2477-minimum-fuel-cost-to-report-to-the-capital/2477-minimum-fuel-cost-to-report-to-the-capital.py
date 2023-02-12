class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adjacency_list = defaultdict(list)
        for a, b in roads:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)            
        total_fuel_cost = [0]        
        def dfs(node, parent):
            people = 1            
            for neighbor in adjacency_list[node]:
                if neighbor == parent:
                    continue
                people += dfs(neighbor, node)                
            if node != 0:
                total_fuel_cost[0] += math.ceil(people / seats)                
            return people        
        dfs(0, None)
        return total_fuel_cost[0]