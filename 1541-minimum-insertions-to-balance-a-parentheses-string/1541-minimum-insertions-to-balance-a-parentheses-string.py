class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                left += 1
            else:
                # Check if it forms a consecutive pair "))"
                if i + 1 < n and s[i+1] == ')':
                    i += 1  # Skip the second ')'
                    if left > 0:
                        left -= 1
                    else:
                        res += 1  # Missing '('
                else:
                    # It's a single ')'
                    if left > 0:
                        left -= 1
                        res += 1  # Missing the second ')' to make "))"
                    else:
                        res += 2  # Missing both '(' and the second ')'
            i += 1
            
        # Each remaining unmatched '(' needs two ')'
        res += left * 2
        return res
