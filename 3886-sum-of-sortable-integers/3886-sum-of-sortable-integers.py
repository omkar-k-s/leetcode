class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        total_sum = 0
        
        # Step 2: Validate each divisor k
        for k in divisors:
            possible = True
            prev_max = float('-inf')
            
            for i in range(0, n, k):
                drops = 0
                block_min = nums[i]
                block_max = nums[i]
                
                # Check cyclic drops and find min/max within the current block
                for j in range(k):
                    val = nums[i + j]
                    next_val = nums[i + (j + 1) % k]
                    
                    if val > next_val:
                        drops += 1
                    if val < block_min:
                        block_min = val
                    if val > block_max:
                        block_max = val
                
                # A block is invalid if it has > 1 drops or breaks global sorted order
                if drops > 1 or block_min < prev_max:
                    possible = False
                    break
                    
                prev_max = block_max
                
            if possible:
                total_sum += k
                
        return total_sum
