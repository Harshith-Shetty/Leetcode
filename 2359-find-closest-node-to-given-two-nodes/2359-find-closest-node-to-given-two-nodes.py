class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        curr = [(node1,1),(node2,2)] 
        visited = [0]*len(edges)
        node = inf
        while curr:  
            new = []
            f = False
            for a,w in curr:
                if visited[a]==0:
                    if edges[a]!=-1:
                        new.append((edges[a],w))
                    visited[a] = w
                elif visited[a]!=w:
                    f = True
                    node = min(a,node)        
            if f:
                return node       
            curr = new 
        return -1
        