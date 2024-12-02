"""

"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        countT = {}
        window = {}
        resLen = float("inf")
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        return s[res[0]: res[1] + 1] if resLen != float('inf') else ""