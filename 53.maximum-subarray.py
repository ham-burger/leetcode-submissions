#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # 新しい値を加味した計算対象
        # 新しい値そのものか、前に演算した値に新しい値を追加したもの
        newNum = nums[0]
        # 計算履歴の中の最大値
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            newNum = max(nums[i], newNum + nums[i])
            # これまでの最高値
            maxTotal = max(maxTotal, newNum)

        return maxTotal	
        # previous_start = 0
        # start = 0
        # result = nums[start]
        # for i in range(len(nums)):
        #     # マイナスになる場合は計算不要
        #     if nums[i] < 0:
        #         continue

        #     if(i != 0 and nums[i - 1] < 0):
        #         previous_start = start
        #         start = i
          
        #     s1 = sum(nums[previous_start:i + 1])
        #     if s1 > result:
        #         result = s1
        #     s2 = sum(nums[start:i + 1])
        #     if s2 > result:
        #         result = s2
 
        # return result
# @lc code=end