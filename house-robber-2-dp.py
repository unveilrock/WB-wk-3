#dp
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        if len(nums)==1:
            return nums[0]
        ppa = pa = ppb = pb = 0
        for i in range(len(nums)-1):
            ppa, pa = pa, max(pa, ppa + nums[i])
            ppb, pb = pb, max(pb, ppb + nums[i+1])
        return max(pa, pb)
