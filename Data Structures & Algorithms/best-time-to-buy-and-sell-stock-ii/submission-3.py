class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # def greedy():
        #     # time: n
        #     # space: 1
        #     p = 0
        #     for i in range(1, len(prices)):
        #         if prices[i-1] < prices[i]:
        #             p+=(prices[i] - prices[i-1])
            
        #     return p
        
        # return greedy()

        # def recursive(i, hold):
        #     # time: 2**n
        #     # space: n
        #     if i == len(prices):
        #         return 0
            
        #     p = recursive(i+1, hold)
        #     if hold:
        #         p = max(p, prices[i] + recursive(i+1, False))
        #     else:
        #         p = max(p, -prices[i] + recursive(i+1, True))

        #     return p

        # return recursive(0, False)

        dp={}
        def dp_top_bottom(i, hold):
            if i == len(prices):
                return 0
            if (i, hold) in dp:
                return dp[(i, hold)]
            
            p = dp_top_bottom(i+1, hold)
            if hold:
                p = max(p, prices[i] + dp_top_bottom(i+1, False))
            else:
                p = max(p, -prices[i] + dp_top_bottom(i+1, True))
            
            dp[i, hold] = p

            return p

        return dp_top_bottom(0, False)


