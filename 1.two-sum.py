#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numsの要素を読み込む
        for i, num in enumerate(nums):
            # 得られた要素とtargetから足りないもう一辺を算出する
            expected = target - num

            # 現在のindex以降でsetを作成する
            set_nums = set(nums[i+1:])

            # listの中に解となる値が存在すればindexを返却,無ければ継続する
            is_exist = expected in set_nums
            if is_exist:
                return [i, nums.index(expected, i+1)]
            else:
                continue

        
# @lc code=end

