class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_no=float('inf')
        max_no =0
        for i in prices:
            if i<min_no:
                min_no=i
            else:
                max_no=max(max_no, i-min_no)
        return max_no

        
        # min_price = float('inf')
        # max_profit = 0

        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)

        # return max_profit










