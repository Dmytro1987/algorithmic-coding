from typing import List


class Solution:

    def averageValue(self, nums: List[int]) -> int:
        nums = [n for n in nums if n % 6 == 0]
        return 0 if len(nums) == 0 else int(sum(nums) / len(nums))

