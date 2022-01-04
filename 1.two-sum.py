#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)
        # numsの要素を読み込む
        for i, num in enumerate(nums):
            # 得られた要素とtargetから足りないもう一辺を算出する
            expected = target - num
            is_exist = expected in set_nums
            # listの中にそれが存在すれば、return,無ければ継続する
            if is_exist:
                # 存在した場合はindexを返却する
                return [i, nums.index(expected)]
            else:
                continue

        
# @lc code=end

