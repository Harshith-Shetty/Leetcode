class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        if m < n:
            a, b = b, a
            m, n = n, m
        res = []
        carry = 0
        for i in range(1, m + 1):
            p = int(a[-i])
            q = int(b[-i]) if i <= n else 0
            carry, val = divmod(p + q + carry, 2)
            res.append(str(val))
        if carry:
            res.append(str(carry))
        return "".join(res[::-1])