class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasksMap, ans = Counter(tasks), 0
        for taskKey in tasksMap:
            if tasksMap[taskKey] == 1:
                return -1
            elif tasksMap[taskKey] % 3 == 0:
                ans += (tasksMap[taskKey] // 3)
            elif (tasksMap[taskKey] + 1) % 3 == 0:
                ans += ((tasksMap[taskKey] + 1) // 3)
            else:
                ans += ((tasksMap[taskKey] + 2) // 3)
        return ans