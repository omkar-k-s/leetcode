class Solution(object):

    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """

        # Convert knowledge into a dictionary
        mp = {}
        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                # Find closing bracket
                j = i + 1
                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Replace with value or '?'
                result.append(mp.get(key, '?'))

                # Move after ')'
                i = j + 1

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)