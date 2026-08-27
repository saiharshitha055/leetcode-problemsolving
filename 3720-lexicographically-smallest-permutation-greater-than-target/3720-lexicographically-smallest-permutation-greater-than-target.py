class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):

            # Try to use target[i] itself
            x = ord(target[i]) - ord('a')

            if count[x] > 0:
                count[x] -= 1
                ans.append(target[i])
                continue

            # Cannot match target[i]
            # Find the smallest character greater than target[i]
            for j in range(x + 1, 26):
                if count[j] > 0:
                    ans.append(chr(j + ord('a')))
                    count[j] -= 1

                    # Put remaining characters in sorted order
                    for c in range(26):
                        ans.extend([chr(c + ord('a'))] * count[c])

                    return ''.join(ans)

            # No character greater than target[i].
            # We need to go back and change an earlier character.
            break

        # If we matched the entire target, it is equal, not greater.
        # Backtrack to find a position we can increase.
        for i in range(len(ans) - 1, -1, -1):

            old = ord(ans[i]) - ord('a')
            count[old] += 1

            for j in range(old + 1, 26):
                if count[j] > 0:
                    result = ans[:i]
                    result.append(chr(j + ord('a')))
                    count[j] -= 1

                    for c in range(26):
                        result.extend([chr(c + ord('a'))] * count[c])

                    return ''.join(result)

        return ""       