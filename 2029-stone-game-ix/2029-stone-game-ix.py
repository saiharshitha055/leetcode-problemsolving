class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1

        a = count[1]
        b = count[2]
        c = count[0]

        if c % 2 == 0:
            return a > 0 and b > 0
        else:
            return abs(a - b) > 2        