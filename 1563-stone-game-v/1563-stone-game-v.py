class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = pref[j + 1] - pref[i]
                
                l, r = i, j - 1
                k_max = i - 1
                while l <= r:
                    m = (l + r) // 2
                    if (pref[m + 1] - pref[i]) * 2 <= total:
                        k_max = m
                        l = m + 1
                    else:
                        r = m - 1
                        
                best = 0
                if k_max >= i and (pref[k_max + 1] - pref[i]) * 2 == total:
                    if k_max > i:
                        best = max(best, max_left[i][k_max - 1])
                    if k_max + 2 <= j:
                        best = max(best, max_right[k_max + 2][j])
                    best = max(best, total // 2 + max(dp[i][k_max], dp[k_max + 1][j]))
                else:
                    if k_max >= i:
                        best = max(best, max_left[i][k_max])
                    if k_max + 2 <= j:
                        best = max(best, max_right[k_max + 2][j])
                        
                dp[i][j] = best
                max_left[i][j] = max(max_left[i][j - 1], total + best)
                max_right[i][j] = max(max_right[i + 1][j], total + best)
                
        return dp[0][n - 1]        