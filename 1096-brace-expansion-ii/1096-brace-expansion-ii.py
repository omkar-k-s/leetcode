class Solution:
    def braceExpansionII(self, expression):

        def multiply(A, B):
            return {a + b for a in A for b in B}

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    inside, i = parse(i + 1)
                    current = multiply(current, inside)

                elif expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                else:
                    current = multiply(current, {expression[i]})
                    i += 1

            result |= current

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)