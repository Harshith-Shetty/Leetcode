class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
      
        a = a & MASK
        b = b & MASK
      
        while b != 0:
            carry = ((a & b) << 1) & MASK
            a = a ^ b
            b = carry
        if a > MAX_INT:
            return ~(a ^ MASK)
        else:
            return a