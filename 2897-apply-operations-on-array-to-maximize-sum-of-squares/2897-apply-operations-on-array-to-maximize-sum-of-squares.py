class Solution:
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bit_counts = [0] * 30

        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    bit_counts[i] += 1

        ans = 0

        for _ in range(k):
            current_num = 0

            for i in range(30):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1

            ans = (ans + current_num * current_num) % MOD

        return ans