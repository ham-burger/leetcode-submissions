#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        return self.hoge(head)

    def hoge(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head
        elif head.val == head.next.val:
            return self.hoge(head.next)
        else:
            node = self.hoge(head.next)
            return ListNode(
                head.val,
                node
            )
 
# @lc code=end