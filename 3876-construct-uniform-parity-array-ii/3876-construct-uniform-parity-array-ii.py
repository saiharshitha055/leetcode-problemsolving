class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        min_val = min(nums1)
        
        # If the minimum element is odd, we can make all elements odd
        if min_val % 2 != 0:
            return True
            
        # If the minimum element is even, we cannot have any odd numbers
        for num in nums1:
            if num % 2 != 0:
                return False
                
        return True       