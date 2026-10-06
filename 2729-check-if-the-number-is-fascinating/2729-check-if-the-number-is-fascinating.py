class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        s = str(n) + str(2 * n) + str(3 * n)

        return len(s) == 9 and set(s) == set("123456789")