class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until we hit the matching '('
                current_substring = []
                while stack and stack[-1] != '(':
                    current_substring.append(stack.pop())
                
                # Pop the opening parenthesis '(' out of the stack
                if stack:
                    stack.pop()
                
                # Push the reversed characters back onto the stack
                for c in current_substring:
                    stack.append(c)
            else:
                # Push regular characters and opening brackets
                stack.append(char)
                
        # Join the stack elements to create the final bracket-free string
        return "".join(stack)
