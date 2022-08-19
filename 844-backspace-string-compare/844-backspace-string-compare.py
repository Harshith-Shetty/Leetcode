class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_array = []
        t_array = []
        for x in s:
            if(x == '#'):
                if(len(s_array)!=0):
                    s_array.pop()
            else:
                s_array.append(x)
        for x in t:
            if(x == '#'):
                if(len(t_array)!=0):
                    t_array.pop()
            else:
                t_array.append(x)
        if(s_array == t_array):
            return True
        else:
            return False