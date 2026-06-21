class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen_val = float('inf')
        profit = 0
        for index, number in enumerate(prices):
            if index == 0:
                lowest_seen_val = number
                continue
            this_profit = number - lowest_seen_val
            if this_profit > profit:
                profit = this_profit
            if number <= lowest_seen_val:
                lowest_seen_val = number
        return profit


