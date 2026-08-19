
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()

            rows[row].add(seat)

        # All rows with no reserved seats can have 2 groups
        answer = (n - len(rows)) * 2

        # Check rows that have reserved seats
        for seats in rows.values():

            count = 0

            # Left block: 2,3,4,5
            if not any(seat in seats for seat in [2, 3, 4, 5]):
                count += 1

            # Right block: 6,7,8,9
            if not any(seat in seats for seat in [6, 7, 8, 9]):
                count += 1

            # If neither left nor right works,
            # try the middle block: 4,5,6,7
            if count == 0:
                if not any(seat in seats for seat in [4, 5, 6, 7]):
                    count = 1

            answer += count

        return answer       