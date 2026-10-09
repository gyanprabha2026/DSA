class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()

        if len(pattern) != len(words):
            return False

        p = {}
        st = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if ch in p and p[ch] != word:
                return False

            if word in st and st[word] != ch:
                return False

            p[ch] = word
            st[word] = ch

        return True 