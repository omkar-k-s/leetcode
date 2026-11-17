class Solution(object):
    def minimumChanges(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        
        # Precompute proper divisors for all lengths from 2 to n
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length // 2 + 1):
                if length % d == 0:
                    divisors[length].append(d)
                    
        # Helper function to find min changes to make s[i..j] a semi-palindrome
        def get_semi_palindrome_cost(i, j):
            length = j - i + 1
            min_changes = float('inf')
            
            for d in divisors[length]:
                changes = 0
                group_len = length // d
                # Check each of the d interleaved groups
                for offset in range(d):
                    left = 0
                    right = group_len - 1
                    while left < right:
                        idx1 = i + offset + left * d
                        idx2 = i + offset + right * d
                        if s[idx1] != s[idx2]:
                            changes += 1
                        left += 1
                        right -= 1
                if changes < min_changes:
                    min_changes = changes
                    
            return min_changes

        # Precompute cost[i][j] for all valid substrings (length >= 2)
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_semi_palindrome_cost(i, j)
                
        # DP[p][j] = min changes to partition s[0..j] into p semi-palindromes
        dp = [[INF] * n for _ in range(k + 1)]
        
        # Base case: 1 partition
        for j in range(1, n):
            dp[1][j] = cost[0][j]
            
        # Fill DP table for 2 to k partitions
        for p in range(2, k + 1):
            # Minimum index j needed for p partitions of length >= 2 is 2*p - 1
            for j in range(2 * p - 1, n):
                # Split point i: prefix s[0..i] has p-1 partitions (min index 2*(p-1) - 1)
                for i in range(2 * (p - 1) - 1, j - 1):
                    if dp[p - 1][i] != INF and cost[i + 1][j] != INF:
                        dp[p][j] = min(dp[p][j], dp[p - 1][i] + cost[i + 1][j])
                        
        return dp[k][n - 1]
