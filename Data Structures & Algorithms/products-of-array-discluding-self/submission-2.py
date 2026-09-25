class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                prod *= num

        ans = []
        for num in nums:
            if zeros > 1:
                ans.append(0)
            elif zeros == 1:
                if num == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
            else:
                ans.append(prod // num)

        return ans