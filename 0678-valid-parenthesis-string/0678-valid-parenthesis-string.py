class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = 0  # Minimum possible open parentheses
        cmax = 0  # Maximum possible open parentheses
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            elif char == '*':
                cmin -= 1  # If treated as ')'
                cmax += 1  # If treated as '('
                
            # If maximum possible open parentheses is negative, 
            # there are too many closing brackets.
            if cmax < 0:
                return False
                
            # cmin cannot be negative; an unmatched ')' cannot carry over
            cmin = max(cmin, 0)
            
        # If cmin is 0, a valid combination exists
        return cmin == 0
