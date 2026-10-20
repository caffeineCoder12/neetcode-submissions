class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            l[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            l[i] *= postfix
            postfix *= nums[i]
        return l