class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums) + 1
        for i in range(0, n):
            if i not in nums:
                return i
# copy paste this in leetcode to run