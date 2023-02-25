class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_so_far = inf
        over_all_profit = 0
        profit_if_sold_today = 0
        for price in prices:
            if price < least_so_far:
                least_so_far = price
            profit_if_sold_today = price-least_so_far
            if(profit_if_sold_today>over_all_profit):
                over_all_profit = profit_if_sold_today
        return over_all_profit