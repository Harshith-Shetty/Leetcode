class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        i, j = m - 1, n - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            result.append(str(carry % 2))
            carry //= 2
        return "".join(result[::-1])