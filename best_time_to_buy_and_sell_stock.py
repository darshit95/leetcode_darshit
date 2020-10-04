class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        
        for i in range(len(prices)):
            
            # For first element, make it as minimum_stock_price vale
            if i == 0:
                min_stock_price = prices[i]
                continue
            
            # If current day price is less than min_stock_price, make it as min_stock_price
            # else calculate profit and compare with best_profit
            
            if prices[i] < min_stock_price:
                min_stock_price = prices[i]
            
            else:
                best_profit = max(best_profit, prices[i] - min_stock_price)
        return best_profit