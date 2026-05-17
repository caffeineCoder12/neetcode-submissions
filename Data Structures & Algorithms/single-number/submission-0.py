class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        for key, value in freq.items():
            if value == 1:
                return key