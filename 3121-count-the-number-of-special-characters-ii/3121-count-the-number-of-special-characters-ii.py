class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Dictionaries to store the last lowercase and first uppercase indices
        last_lower = {}
        first_upper = {}
        
        # Traverse the string to record the indices
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            elif char.isupper():
                if char not in first_upper:
                    first_upper[char] = i
                    
        special_count = 0
        
        # Check all lowercase letters present in the string
        for char in last_lower:
            upper_char = char.upper()
            # Condition 1: Both lowercase and uppercase must exist
            # Condition 2: Last lowercase index must be before the first uppercase index
            if upper_char in first_upper and last_lower[char] < first_upper[upper_char]:
                special_count += 1
                
        return special_count
