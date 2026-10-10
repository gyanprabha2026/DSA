class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        freq = {}
        ans = []

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for num, count in freq.items():
            if count > n//3:
                ans.append(num)

        return ans