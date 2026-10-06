class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        mismatched_open = 0
        mismatched_close = 0
        
        for char in s:
            if char == '(':
                mismatched_open += 1
            elif char == ')':
                if mismatched_open > 0:
                    # Current closing parenthesis pairs up with a previous open one
                    mismatched_open -= 1
                else:
                    # No matching open parenthesis available, so this close is unmatched
                    mismatched_close += 1
                    
        return mismatched_open + mismatched_close
