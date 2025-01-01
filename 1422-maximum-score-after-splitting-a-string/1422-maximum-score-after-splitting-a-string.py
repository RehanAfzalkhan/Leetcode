class Solution:
    def maxScore(self, s: str) -> int:
        left = ""
        right = ""
        max_score = 0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            max_score = max(left.count('0') + right.count('1'),max_score)
        return max_score 