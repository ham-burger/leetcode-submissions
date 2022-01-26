#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # print(f"sum {targetSum}")
        if root == None:
            # print("root is None")
            return False
        
        diff = targetSum - root.val
        leftIsNone = root.left == None
        rightIsNone = root.right == None
        if not leftIsNone:
            leftResult = self.hasPathSum(root.left, diff)
            if leftResult:
                # print(f"left True {root.left} {diff}")
                return True
        if not rightIsNone:
            rightResult=self.hasPathSum(root.right, diff)
            if rightResult:
                # print(f"right True {root.right} {diff}")
                return True

        if diff == 0 and leftIsNone and rightIsNone:
            # print(f"True {targetSum} {root.val}")
            return True

        # print(f"False diff {diff} right: {root.right} left {root.left}")
        return False
# @lc code=end

