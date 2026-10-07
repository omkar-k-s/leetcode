class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Helper function to check if a string has balanced parentheses
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # Initialize the current level with the input string
        # Using a set automatically prevents duplicate strings at each level
        level = {s}
        
        while level:
            # Filter out and keep only the valid strings in the current level
            valid_strings = list(filter(isValid, level))
            
            # If we found any valid strings, they are guaranteed to have the minimum removals
            if valid_strings:
                return valid_strings
            
            # If no valid strings are found, generate the next level by removing one parenthesis
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    # Only attempt to remove parentheses, skip letters
                    if string[i] in ('(', ')'):
                        next_level.add(string[:i] + string[i+1:])
            
            level = next_level
            
        return [""]
