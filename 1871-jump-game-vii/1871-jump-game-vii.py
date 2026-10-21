from collections import deque

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        # If the last character is '1', it's impossible to reach it
        if s[-1] == '1':
            return False
            
        queue = deque([0])
        far = 0  # Tracks the furthest index explored to avoid duplicate work
        n = len(s)
        
        while queue:
            curr = queue.popleft()
            
            # If we reached the last index, return True
            if curr == n - 1:
                return True
                
            # Define the valid range of jumps from the current position
            start = max(curr + minJump, far + 1)
            end = min(curr + maxJump, n - 1)
            
            # Iterate through the valid window
            for j in range(start, end + 1):
                if s[j] == '0':
                    queue.append(j)
                    
            # Update 'far' so the next nodes don't re-examine indices we just covered
            far = max(far, curr + maxJump)
            
        return False
