class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = []
        prev = 0
        output  = [] 
        tasks= sorted((tasks,i) for i,tasks in enumerate(tasks))
        for (m,n), i in tasks:
            while arr and prev < m:
                p,j,k = heappop(arr)
                prev = max(k,prev)+p
                output.append(j)
            heappush(arr,(n,i,m))
        return output+[i for _, i, _ in sorted(arr)]