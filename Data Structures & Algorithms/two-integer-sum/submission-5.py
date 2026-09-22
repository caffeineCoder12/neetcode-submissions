class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,value in enumerate(nums):
            hashmap[i] = target - value
        for v in hashmap.items():
            if v[1] in nums and v[0] != nums.index(v[1]):
                return sorted([v[0],nums.index(v[1])])