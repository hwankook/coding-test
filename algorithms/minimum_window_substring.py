from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ''

        counter = Counter(t)
        MIN, MAX = len(s) + 1, len(t)

        start = 0
        for end in range(len(s)):
            if 0 < counter[s[end]]:
                MAX -= 1
            counter[s[end]] -= 1

            while 0 == MAX:
                L = end - start + 1
                if len(t) <= L < MIN:
                    MIN = L
                    result = s[start:end + 1]

                counter[s[start]] += 1
                if 0 < counter[s[start]]:
                    MAX += 1

                start += 1

        return result
