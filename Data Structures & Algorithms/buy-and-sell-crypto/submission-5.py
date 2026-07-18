class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_price_idx = 1
        buy_price_idx = 0
        profit=0
        while sell_price_idx<len(prices):
            if prices[buy_price_idx] < prices[sell_price_idx]:
                sum =  (prices[sell_price_idx] - prices[buy_price_idx])
                profit = max(sum,profit)
            else:
                buy_price_idx = sell_price_idx
            sell_price_idx+=1
        return profit            

        