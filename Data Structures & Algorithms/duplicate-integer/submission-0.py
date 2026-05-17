class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checking = {}
        for i in nums:
            if i in checking:
                return True
            checking[i] = True
        return False