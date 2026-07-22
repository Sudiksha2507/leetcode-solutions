class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = []
        rev = []

        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower())
                rev = chars[::-1]

        return rev == chars
