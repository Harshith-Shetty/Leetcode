class Solution(object):
    def uniqueOccurrences(self, arr):
        map = {}
        occurence = set()
        for i in arr:
            if i in map:
                map[i] = map[i] + 1
            else:
                map[i] = 1
        for key,value in map.items():
            occurence.add(value)
        return len(map) == len(occurence)

        