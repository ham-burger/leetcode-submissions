#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        newNum = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            # 今のindexの値と、前のindexを含んで作り得る最大値に今のindexの値を足したら、どちらが大きくなるのか検証する
            newNum = max(nums[i], newNum + nums[i])
            # これまで検証した最大値と今のindexで取りうる最大値を比較する
            maxTotal = max(maxTotal, newNum)
        return maxTotal	
# @lc code=end