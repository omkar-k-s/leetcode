class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the shorter array to optimize the binary search range O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_half = (m + n + 1) // 2
        
        while low <= high:
            partition_x = (low + high) // 2
            partition_y = total_half - partition_x
            
            # Edge cases: handle if partitions are at the absolute boundaries
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == m else nums1[partition_x]
            
            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == n else nums2[partition_y]
            
            # Check if we found the correct partition alignment
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # If the total number of elements is odd
                if (m + n) % 2 != 0:
                    return float(max(max_left_x, max_left_y))
                # If the total number of elements is even
                else:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
            
            # If we are too far right in nums1, move left
            elif max_left_x > min_right_y:
                high = partition_x - 1
            # If we are too far left in nums1, move right
            else:
                low = partition_x + 1
                
        return 0.0
