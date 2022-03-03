#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        harf=start+end//2

        # whileで良い
        while True:
            if(start==end and nums[start]!=target):
                return -1
            if(nums[start]==target):
                return start
            elif(nums[end]==target):
                return end
            elif(nums[harf]==target):
                return harf

            if(nums[start]<=nums[harf]):
                if(nums[start]<=target<=nums[harf]):
                    end=harf
                else:
                    start=harf+1
            elif(nums[harf+1]<=nums[end]):
                if(nums[harf+1]<=target<=nums[end]):
                    start=harf+1
                else:
                    end=harf
            harf=(start+end)//2

# @lc code=end

