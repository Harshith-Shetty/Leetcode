class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        response = [0] * n
        node2edges = [[] for _ in range(n)]
        for edge in edges:
            node2edges[edge[0]].append(edge[1])
            node2edges[edge[1]].append(edge[0])
            
        def dfs(nodeId: int, parentNodeId: int, labelCounter: List[int]) -> None:
            nodeLabelId = ord(labels[nodeId]) - 97
            before = labelCounter[nodeLabelId]
            labelCounter[nodeLabelId] += 1
            for nextNodeId in node2edges[nodeId]:
                if nextNodeId == parentNodeId:
                    continue
                dfs(nextNodeId, nodeId, labelCounter)
            response[nodeId] = labelCounter[nodeLabelId] - before
        dfs(0, -1, [0] * 26)
        return response