import heapq

class Solution(object):
    def minOperations(self, nums, x, k):
        """
        :type nums: List[int]
        :type x: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # cost[i] stores the minimum operations to equalize nums[i : i + x]
        cost = [float('inf')] * n
        
        left_max_heap = []   # Max-heap for the lower half (inverted values)
        right_min_heap = []  # Min-heap for the upper half
        
        left_sum = 0
        right_sum = 0
        left_size = 0
        right_size = 0
        
        # Track counts of elements lazily waiting for deletion
        to_delete = {}
        
        def prune():
            # Remove elements from top of left max-heap if they are marked for deletion
            while left_max_heap and to_delete.get(-left_max_heap[0], 0) > 0:
                to_delete[-left_max_heap[0]] -= 1
                heapq.heappop(left_max_heap)
            # Remove elements from top of right min-heap if they are marked for deletion
            while right_min_heap and to_delete.get(right_min_heap[0], 0) > 0:
                to_delete[right_min_heap[0]] -= 1
                heapq.heappop(right_min_heap)

        for i in range(n):
            # 1. Insert the incoming element
            val = nums[i]
            if not left_max_heap or val <= -left_max_heap[0]:
                heapq.heappush(left_max_heap, -val)
                left_sum += val
                left_size += 1
            else:
                heapq.heappush(right_min_heap, val)
                right_sum += val
                right_size += 1
                
            # 2. Handle the outgoing element (sliding out of window)
            if i >= x:
                out_val = nums[i - x]
                to_delete[out_val] = to_delete.get(out_val, 0) + 1
                
                # Determine which heap the outgoing element logically belongs to
                if out_val <= -left_max_heap[0]:
                    left_size -= 1
                    left_sum -= out_val
                else:
                    right_size -= 1
                    right_sum -= out_val
            
            # 3. Maintain size balancing
            # For a window of size w, left_size must equal (w + 1) // 2
            w = min(i + 1, x)
            target_left_size = (w + 1) // 2
            
            prune()
            
            # Rebalance heaps if left half has too few elements
            while left_size < target_left_size:
                move_val = heapq.heappop(right_min_heap)
                if to_delete.get(move_val, 0) > 0:
                    to_delete[move_val] -= 1
                else:
                    heapq.heappush(left_max_heap, -move_val)
                    left_sum += move_val
                    right_sum -= move_val
                    left_size += 1
                    right_size -= 1
                prune()
                
            # Rebalance heaps if left half has too many elements
            while left_size > target_left_size:
                move_val = -heapq.heappop(left_max_heap)
                if to_delete.get(move_val, 0) > 0:
                    to_delete[move_val] -= 1
                else:
                    heapq.heappush(right_min_heap, move_val)
                    right_sum += move_val
                    left_sum -= move_val
                    right_size += 1
                    left_size -= 1
                prune()
                
            prune()
            
            # 4. Record L1 cost if the sliding window is fully formed
            if i >= x - 1:
                median = -left_max_heap[0]
                current_cost = (median * left_size - left_sum) + (right_sum - median * right_size)
                cost[i - x + 1] = current_cost

        # 5. Interval Selection Dynamic Programming
        # dp[i][j] = min operations using prefix up to index i to pick j valid windows
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Option 1: Skip the current element position
                dp[i][j] = dp[i - 1][j]
                
                # Option 2: Place a window ending exactly at index i - 1
                if i >= x:
                    window_start = i - x
                    if cost[window_start] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[window_start][j - 1] + cost[window_start])
                        
        return dp[n][k]
