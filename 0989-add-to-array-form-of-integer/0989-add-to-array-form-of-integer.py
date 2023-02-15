class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = ""
        for i in num:
            l = l + str(i)
        l = str(int(l) + k)
        res =[]
        for i in l:
            res.append(int(i))
        return res
        