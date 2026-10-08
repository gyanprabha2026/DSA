class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        
        n = len(arr)
        i = 0

        while i < n:

            for j in range(i+1, n):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True
            
            i += 1
        
        return False