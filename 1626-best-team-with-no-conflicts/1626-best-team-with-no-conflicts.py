class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new_list = sorted(zip(ages, scores)) 
        visited = [new_list[0][1]] 
        dp = [new_list[0][1]] 
        ans = new_list[0][1] 

        for i in range(1,len(new_list)):
            s = new_list[i][1]
            index =bisect_right(visited, s) 
            curr = max(dp[:index]) + s if index else s 
            ans = max(ans, curr)
            visited.insert(index, s) 
            dp.insert(index,curr)
        return ans