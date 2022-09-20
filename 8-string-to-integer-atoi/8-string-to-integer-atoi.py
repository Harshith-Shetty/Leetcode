class Solution:
    def myAtoi(self, s: str) -> int:
        str_list = s.split()
        
        if not str_list:
            return 0
                
        num_str = str_list[0]
        sign = -1 if num_str[0] == '-' else +1
        start = 1 if num_str[0] in '-+' else 0
        
        num = 0
        int_boundary =  0x80000000 if sign == -1 else 0x7fffffff # 2147483648 or 2147483647
        
        for i in range(start, len(num_str)):
            ord_digit = ord(num_str[i])
            if ord_digit < 48 or ord_digit > 57:
                break
            
            num *= 10
            num += ord_digit - 48
            
            if num >= int_boundary:
                num = int_boundary
                break
        
        return num * sign
