class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        c = list(s)
        left = 0
        right = len(c) - 1

        while left < right:
            if not c[left].isalpha():
                left += 1
            elif not c[right].isalpha():
                right -= 1
            else:
                c[left], c[right] = c[right], c[left]
                left += 1
                right -= 1

        return "".join(c)
