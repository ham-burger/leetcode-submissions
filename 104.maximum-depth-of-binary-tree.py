#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calc(root, 0)
    
    def calc(self, root: Optional[TreeNode], depth: int):
        if root == None:
            return depth

        right = self.calc(root.right, depth)
        left = self.calc(root.left, depth)
        if right > left:
            return right + 1
        else:
            return left + 1

# @lc code=end

