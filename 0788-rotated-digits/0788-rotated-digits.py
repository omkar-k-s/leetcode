class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        
        # Define digit categories
        invalid_digits = {'3', '4', '7'}
        good_digits = {'2', '5', '6', '9'}
        
        for i in range(1, n + 1):
            s = str(i)
            # Check if any digit makes the number completely invalid
            if any(d in invalid_digits for d in s):
                continue
            # Check if at least one digit forces the number to change value
            if any(d in good_digits for d in s):
                count += 1
                
        return count
