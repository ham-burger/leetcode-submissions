#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        right = self.minDepth(root.right) + 1
        left = self.minDepth(root.left) + 1
        if root.left == None:
            return right
        if root.right == None:
            return left
        
        return min(right, left)
# @lc code=end

