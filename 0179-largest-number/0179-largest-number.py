class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            a = str(a)
            b = str(b)

            if a + b > b + a:
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))

        result = ''.join(map(str, nums))

        if result[0] == '0':
            return '0'

        return result