from itertools import accumulate

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Calculate the prefix sums of the stones
        # S[i] represents the score a player gets if they remove stones up to index i
        S = list(accumulate(stones))
        
        # Base case: if a player decides to take all remaining stones (index n-1)
        # The game ends, and the current player gets S[-1], opponent gets 0.
        dp = S[-1]
        
        # Iterate backwards from the second to last possible choice down to index 1.
        # We stop at 1 because a player must take x > 1 stones, meaning index 0 is invalid.
        for i in range(len(stones) - 2, 0, -1):
            # A player has two choices:
            # 1. Don't stop at this prefix sum (which is equivalent to taking the best future choice: dp)
            # 2. Stop at this prefix sum (score S[i]) and give the next turn to the opponent (opponent gets dp)
            if S[i] - dp > dp:
                dp = S[i] - dp
                
        return dp        