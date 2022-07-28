class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged_array =[]
        if(len(intervals)==1):
            return intervals
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)):
            if(len(merged_array)==0 or merged_array[-1][1] < intervals[i][0]):
                list=[]
                list.append(intervals[i][0])
                list.append(intervals[i][1])
                merged_array.append(list)
            else:
                merged_array[-1][1] = max(merged_array[-1][1],intervals[i][1])
        return merged_array