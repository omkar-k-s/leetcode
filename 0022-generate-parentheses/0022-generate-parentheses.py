class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # Base case: if the current string has reached the maximum length
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Rule 1: We can add an opening parenthesis if we haven't reached 'n'
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Rule 2: We can add a closing parenthesis if it matches an open one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result
