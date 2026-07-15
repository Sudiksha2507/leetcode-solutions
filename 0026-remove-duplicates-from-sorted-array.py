class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        seen=[]

        for num in nums:

            if num not in seen:

                seen.append(num)

        for i in range(len(seen)):

            nums[i]=seen[i]

        return len(seen)
