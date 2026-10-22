class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in freq:
            if freq[ch] < k:
                parts = s.split(ch)
                res = 0

                for part in parts:
                    res = max(res, self.longestSubstring(part, k))

                return res

        return len(s)