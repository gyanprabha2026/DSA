class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        v = {}
        c = {}
        check = "AEIOUaeiou"

        for i in s:
            if i in check:
                v[i] = v.get(i, 0) + 1
            else:
                c[i] = c.get(i, 0) + 1

        return max(v.values(), default=0) + max(c.values(), default=0)