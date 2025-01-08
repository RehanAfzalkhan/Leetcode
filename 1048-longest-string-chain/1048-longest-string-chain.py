class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Step 1: Sort the words by length
        words.sort(key=len)
        
        # Step 2: Initialize dp and max_chain
        dp = {}
        max_chain = 1
        
        # Step 3: Process each word
        for word in words:
            dp[word] = 1  # Minimum chain length is 1 (trivial chain)
            for i in range(len(word)):
                # Generate a predecessor by removing the i-th character
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            max_chain = max(max_chain, dp[word])
        
        return max_chain