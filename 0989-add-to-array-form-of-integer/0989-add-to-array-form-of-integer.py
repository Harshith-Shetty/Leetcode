class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if not num:
            return [int(d) for d in str(k)]
        carry = 0
        res = []
        for i in range(len(num)-1, -1, -1):
            total = num[i] + carry + (k % 10)
            carry = total // 10
            res.append(total % 10)
            k //= 10
        while k > 0:
            total = carry + (k % 10)
            carry = total // 10
            res.append(total % 10)
            k //= 10
        if carry > 0:
            res.append(carry)
        return res[::-1]