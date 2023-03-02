class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        mychar = chars[0]
        count = 0
        length = len(chars)
        chars.append(" ") 
        for i in range(length+1): 
            char = chars.pop(0)
            if char == mychar: 
                count += 1
            else:
                if count == 1: 
                    chars.append(mychar) 
                elif count > 1:
                    chars.append(mychar)
                    chars += (list(str(count))) 
                mychar = char 
                count = 1 
        return len(chars)