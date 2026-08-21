class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        pie = []
        
        def dfs(i, current_lcm, cnt):
            if i == len(coins):
                if cnt > 0:
                    pie.append((current_lcm, 1 if cnt % 2 == 1 else -1))
                return
            
            dfs(i + 1, current_lcm, cnt)
            dfs(i + 1, math.lcm(current_lcm, coins[i]), cnt + 1)
            
        dfs(0, 1, 0)
        
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            count = 0
            for l, sign in pie:
                count += sign * (mid // l)
                
            if count >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
        