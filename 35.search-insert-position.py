#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        last = len(nums) - 1

        # while(True):
        #     # 範囲外なら確定
        #     if(nums[start] >= target):
        #         return start
        #     elif(nums[last] == target):
        #         return last
        #     elif(nums[last] < target):
        #         return last +1
        #     else:
        #         # 範囲内なら範囲を絞り込んでいく
        #         diff = last - start
        #         index = start + (diff // 2)
        #         harf = nums[index]

        #         # 丁度範囲の境目の場合は確定
        #         if(harf < target):
        #             start = index + 1
        #         else:
        #             last = index - 1
        # while(start < last):
        #     # diff = last - start
        #     # middle = start + (diff // 2)
        #     middle = (start + last) // 2
        #     if(nums[middle] == target):
        #         return middle
        #     elif(middle < target):
        #         start = middle + 1
        #     else:
        #         last = middle - 1

        # return start

        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# @lc code=end

