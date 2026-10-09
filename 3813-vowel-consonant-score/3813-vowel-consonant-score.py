class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        
        v = 0
        c = 0
        check = "AEIOUaeiou"

        for i in s:
            if i.isalpha():
                if i in check:
                    v += 1
                else:
                    c += 1

        if c == 0:
            return 0

        return v // c