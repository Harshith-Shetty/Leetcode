class Solution:
    def reverseVowels(self, s: str) -> str:
        appeared_vowel =[]
        vowels = {"a", "e", "i", "o", "u"}
        for i in s:
            if(i.lower() in vowels):
                appeared_vowel.append(i)
        a = 0
        b = len(appeared_vowel) - 1
        print("b")
        print(b)
        s_list = list(s)
        for i in range(len(s_list)):
            if(a<=b):
                if(s_list[i] == appeared_vowel[a]):
                    print(a)
                    print(appeared_vowel[b-a])
                    s_list[i] = appeared_vowel[b-a]
                    a = a + 1 
        s = ''.join(s_list)
        return s
            