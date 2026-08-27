class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # i, not i + 1, because we can reuse the same number
                backtrack(i, remaining - candidates[i], current)

                current.pop()

        backtrack(0, target, [])
        return result