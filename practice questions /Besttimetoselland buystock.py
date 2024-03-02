class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = []
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] > prices[i]:
        #             res = prices[j] - prices[i]
        #             maxProfit.append(res)
        #         else:
        #             i = j
        # return max(maxProfit, default = 0)


        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l=r
            r+=1
        return maxProfit
        

    

                






            
      


        
            
            

