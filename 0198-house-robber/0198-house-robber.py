class Solution:
    
    def hr(self, i, nums, dp):
            if i >= len(nums):
                return 0
            
            if dp[i] != -1:
                return dp[i]

            fi = nums[i] + self.hr(i+2, nums, dp)
            se = self.hr(i+1, nums, dp)

            dp[i] = max(fi, se)
            return dp[i]
            
    def rob(self, nums):
        
        dp = [-1] * len(nums)
        return self.hr(0, nums, dp)
        



                