class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        # First half
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        # Second half
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Odd number of ? -> Alice always wins
        if (left_q + right_q) % 2 == 1:
            return True

        # Even number of ?
        return left_sum - right_sum != 9 * (right_q - left_q) // 2