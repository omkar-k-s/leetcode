class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign based on current depth parity, then increase depth
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrease depth first, then assign to match the opening brace
                depth -= 1
                ans.append(depth % 2)
                
        return ans
