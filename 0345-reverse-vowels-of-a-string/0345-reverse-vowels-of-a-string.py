class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s = list(s)
        i = 0
        j = len(s) - 1
        check = "AEIOUaeiou"

        while i < j:

            if s[i] in check and s[j] in check:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            elif s[i] in check and s[j] not in check:
                j -= 1

            elif s[i] not in check and s[j] in check:
                i += 1

            else:
                i += 1
                j -= 1
        
        return "".join(s)