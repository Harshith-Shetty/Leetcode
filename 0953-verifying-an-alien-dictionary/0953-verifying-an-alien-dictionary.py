class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hm = {ch: i for i, ch in enumerate(order)}

        prev_repr = list(hm[ch] for ch in words[0])
        for i in range(1, len(words)):
            cur_repr = list(hm[ch] for ch in words[i])

            if cur_repr < prev_repr:
                return False

            prev_repr = cur_repr

        return True