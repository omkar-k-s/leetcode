class Solution:
    def isValid(self, s):

        # Map each closing bracket to its corresponding opening bracket
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the top element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were properly matched
        return not stack
