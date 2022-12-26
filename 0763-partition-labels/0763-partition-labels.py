class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        dict = {}
        for i,j in enumerate(s):
            dict[j]=i
        start = 0
        end = 0
        for i,j in enumerate(s):
            end = max(end,dict[j])
            if(i==end):
                output.append(end-start+1)
                start = end + 1
        return output