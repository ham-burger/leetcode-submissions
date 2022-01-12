#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    """
    (1)
    input
    [1,3,5,6]
    5

    process
    
    3
    5
    
    output
    0

    (2)
    input
    [1,3,5,6]
    2

    process
    3
    1

    output
    1

    (4)
    input
    [1,3,5,6,8]
    4

    process
    5
    3

    output
    2

    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        last = len(nums) - 1

        while(True):
            # 範囲外なら確定
            if(nums[start] >= target):
                return start
            elif(nums[last] == target):
                return last
            elif(nums[last] < target):
                return last + 1

            # 範囲内なら範囲を絞り込んでいく
            diff = last - start
            index = start + (diff // 2)
            harf = nums[index]

            # 丁度範囲の境目の場合は確定
            if(harf == target):
                return index
            elif(harf < target):
                start = index + 1
            else:
                last = index - 1

        # # todo: 終了条件変更する
        # if(nums[start] < target):
        #     return last + 1
        # else:
        #     return start
#
# @lc code=end

