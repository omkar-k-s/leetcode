class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Stack initialized with -1 to serve as the base/sentinel for the first valid match
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the open parenthesis
                stack.append(i)
            else:
                # Pop the last element (either a matching '(' index or the current base)
                stack.pop()
                
                if not stack:
                    # If stack is empty, this ')' has no matching '('
                    # Push current index as the new base boundary
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
