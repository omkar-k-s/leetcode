class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :type rtype: str
        """
        # If the required sum exceeds the maximum possible sum for 'num' digits
        if sum > 9 * num:
            return ""
        
        # Calculate how many 9s we can fit and the remaining digit
        nines = sum // 9
        remainder = sum % 9
        
        # Build the list of digits starting with the largest values
        digits = ["9"] * nines
        if remainder > 0:
            digits.append(str(remainder))
            
        # Fill the remaining length with zeros
        zeros_needed = num - len(digits)
        digits.extend(["0"] * zeros_needed)
        
        # Since it's already constructed in descending order, just join into a string
        return "".join(digits)
