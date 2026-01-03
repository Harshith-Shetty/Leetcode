class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        track = []
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                track.append(i)
            else:
                if len(track) == 0:
                    return False
                prev = track[-1]
                track.pop()
                if not (( i == ')' and prev == '(') or (i == '}' and prev == '{') or (i == ']' and prev == '[')):
                    return False
                
        return len(track) == 0