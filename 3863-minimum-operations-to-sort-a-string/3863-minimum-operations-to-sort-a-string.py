class Solution:
    def minOperations(self, s: str) -> int:

   
        # If the string is already sorted
        if all(a <= b for a, b in pairwise(s)):
            return 0
        
        # If length is 2 and not sorted, it's impossible
        if len(s) == 2:
            return -1
        
        mn, mx = min(s), max(s)
        
        # If min is already at the beginning or max is at the end
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # If min or max exists in the interior (excluding endpoints)
        if any(c in (mn, mx) for c in s[1:-1]):
            return 2
            
        return 3      