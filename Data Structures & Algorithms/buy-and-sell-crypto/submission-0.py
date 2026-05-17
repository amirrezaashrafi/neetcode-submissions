class Solution:
    def maxProfit(self, prices):
        max_pro = 0
        min_price = prices[0]

        for today_price in prices:
            profit = today_price - min_price
            max_pro = max(max_pro, profit)
            min_price = min(min_price, today_price)

        return max_pro    