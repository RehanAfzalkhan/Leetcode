class Solution:
    def integerReplacement(self, n: int) -> int:
        # recursive approach
        memo = {}

        def dfs(x):
            if x == 1:
                return 0
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                result = 1 + dfs(x//2)
            else:
                result = 1 + min(dfs(x - 1), dfs(x + 1))
            memo[x] = result
            return result

        return dfs(n)