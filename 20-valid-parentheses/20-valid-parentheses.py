class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {')':'(', '}':'{', ']':'['}
        st = []
        for e in s:
            if st and (e in map_dict and st[-1] == map_dict[e]):
                st.pop()
            else:
                st.append(e)
        return not st