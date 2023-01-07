class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        end = 0 
        sum = 0
        length = 0
        while start<len(gas) and length < len(gas):
            sum += gas[end]-cost[end]
            length +=1
            while start<len(gas) and sum < 0:
                sum -= gas[start] - cost[start]
                start +=1
                length-=1
            end+=1
            end = end % len(gas)
        if length == len(gas):
            return start
        return -1