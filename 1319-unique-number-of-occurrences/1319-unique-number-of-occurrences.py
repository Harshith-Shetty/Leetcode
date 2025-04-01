class Solution(object):
    def uniqueOccurrences(self, arr):
        freq_map = {}
        for i in arr:
            freq_map[i] = freq_map.get(i,0) + 1
        return len(freq_map) == len(set(freq_map.values()))

        