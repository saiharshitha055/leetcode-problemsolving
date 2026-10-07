

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        from collections import deque

        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i, char in enumerate(current):
                if char not in ('(', ')'):
                    continue

                if i > 0 and current[i] == current[i - 1]:
                    continue

                next_str = current[:i] + current[i + 1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result