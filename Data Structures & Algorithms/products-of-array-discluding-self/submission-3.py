class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]*len(nums)
        for i in range(1,len(nums)):
            l[i] *= (nums[i-1]*l[i-1])
        a = 1
        for i in range(len(nums)-1,-1,-1):
            l[i] *= a
            a *= nums[i]
        return l