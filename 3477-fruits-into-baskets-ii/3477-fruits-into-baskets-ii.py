class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        used = []

        for fruit in fruits:

            for j in range(len(baskets)):

                if j not in used and fruit <= baskets[j]:
                    used.append(j)
                    break
        
        return len(fruits) - len(used)
