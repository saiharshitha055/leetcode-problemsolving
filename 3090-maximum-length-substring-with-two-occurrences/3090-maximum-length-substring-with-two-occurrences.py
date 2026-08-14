class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        answer = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer 