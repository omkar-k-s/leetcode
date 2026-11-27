class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        min_price = min(price for _, price in items)
        
        # Step 1: Precompute total copies gained from buying 1st copy of item i
        gains = [1] * n
        for i in range(n):
            factor_i = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % factor_i == 0:
                    gains[i] += 1
                    
        # Step 2: 0/1 Knapsack for choosing which distinct items to buy at least once
        # dp[c] = max copies obtained using exact cost c
        dp = [-1] * (budget + 1)
        dp[0] = 0
        
        for i in range(n):
            price = items[i][1]
            gain = gains[i]
            # Traverse backwards for 0/1 Knapsack
            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    dp[c] = max(dp[c], dp[c - price] + gain)
                    
        # Step 3: Spend any remaining budget greedily on the cheapest item
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                extra_copies = (budget - c) // min_price
                ans = max(ans, dp[c] + extra_copies)
                
        return ans
