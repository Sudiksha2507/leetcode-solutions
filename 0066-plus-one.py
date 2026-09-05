class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        int = 0

        for num in digits:
            int = int * 10 + num

        int = int + 1

        while int > 0:
            num = int % 10
            res.append(num)
            int //= 10

        res.reverse()
        return res
