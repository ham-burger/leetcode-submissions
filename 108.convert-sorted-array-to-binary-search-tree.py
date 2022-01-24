#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if nums == []:
            return None
        harf = (len(nums) - 1) // 2
        node = TreeNode(nums[harf])
        node.left = self.sortedArrayToBST(nums[:harf])
        node.right = self.sortedArrayToBST(nums[harf+1:])
        return node
# @lc code=end
