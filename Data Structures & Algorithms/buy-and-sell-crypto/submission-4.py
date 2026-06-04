class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l,r = 0,1
        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
                r+=1
                #print("l =",l,"r =",r)
            elif prices[l] < prices[r]:
                p = max(p,prices[r]-prices[l])
                r+=1
                #print("l =",l,"r =",r)
                #print("p =",p)
            elif prices[l] == prices[r]:
                r+=1
        return p