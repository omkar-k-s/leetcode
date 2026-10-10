class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2
        # Calculate absolute differences
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        # If there are no differences, the sum of squared differences is already 0
        if max_diff == 0:
            return 0
            
        # Create a bucket array to record the frequency of each difference
        bucket = [0] * (max_diff + 1)
        for d in diffs:
            bucket[d] += 1
            
        # Greedily shift differences down from max_diff to 1
        for d in range(max_diff, 0, -1):
            if bucket[d] == 0:
                continue
            
            # Determine how many items we can reduce by 1 at this level
            ops = min(bucket[d], k)
            bucket[d] -= ops
            bucket[d - 1] += ops
            k -= ops
            
            # If we run out of modifications, stop early
            if k == 0:
                break
        
        # Calculate the final minimum sum of squared differences
        ans = sum(count * (d ** 2) for d, count in enumerate(bucket))
        return ans
