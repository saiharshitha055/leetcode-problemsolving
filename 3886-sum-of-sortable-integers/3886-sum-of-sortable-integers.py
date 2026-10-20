class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:

        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Helper to find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
                    
        def is_cyclic_shift(B: list[int], S: list[int], k: int) -> bool:
            """
            Returns True if block B is a cyclic rotation of sorted block S.
            """
            if k == 1:
                return B[0] == S[0]
            
            # Count local drops in B (cyclically)
            drops = 0
            drop_idx = -1
            for i in range(k):
                if B[i] > B[(i + 1) % k]:
                    drops += 1
                    drop_idx = i
                    if drops > 1:
                        return False
            
            if drops == 0:
                # B is already non-decreasing, check if it equals S
                return B == S
            
            # If 1 drop, the rotated version starts at (drop_idx + 1)
            shift = drop_idx + 1
            rotated = B[shift:] + B[:shift]
            return rotated == S

        ans = 0
        
        for k in divisors:
            possible = True
            for i in range(0, n, k):
                B = nums[i : i + k]
                S = sorted_nums[i : i + k]
                if not is_cyclic_shift(B, S, k):
                    possible = False
                    break
            
            if possible:
                ans += k
                
        return ans      