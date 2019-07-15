#recursion and memoization
class Solution:
    def rob(self, nums) -> int:
        memo = dict()
        memo2 = dict()
        l = len(nums)
        if l==1:
            return nums[0]
        
    
        def robhelp1(i: int):
            if i>=l:
                return 0
            if i in memo:
                return memo[i]
            if i==l-1:
                return nums[i]
            
            memo[i] = max(robhelp1(i+1),nums[i] + robhelp1(i+2))
            return max(robhelp1(i+1),nums[i] + robhelp1(i+2))

        def robhelp2(i: int):
            if i >=l-1:
                return 0
            if i in memo2:
                return memo2[i]
            if i == l - 2:
                return nums[i]
            
            memo2[i] = max(robhelp2(i + 1), nums[i] + robhelp2(i + 2))
            return max(robhelp2(i + 1), nums[i] + robhelp2(i + 2))

        return max(robhelp1(1),robhelp2(0))
