#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if(len(nums)==0):
            return
        # 数値の小さい方から演算していく
        for n in range(len(nums)):
            # 先頭の桁に来るまで該当する値を算出できない場合は一番小さい値にする
            if(n+1==len(nums)):
                nums.sort()
                break

            i=(n+1)*-1
            next_i=i-1

            if(nums[next_i]<nums[i]):
                f=filter(lambda x:x>nums[next_i],nums[i:])
                m=min(f)
                change_i=nums[i:].index(m) + i
                nums[next_i],nums[change_i]=nums[change_i],nums[next_i]
                sliced=nums[i:]
                sliced.sort()
                del nums[i:]
                nums.extend(sliced)
                break

# @lc code=end

