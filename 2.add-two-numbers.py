#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        if not l1:
            l1=ListNode()
        if not l2:
            l2=ListNode()
        
        val=l1.val+l2.val
        result=ListNode(val%10)
        advance=val//10
        if advance!=0:    
            if not l1.next:
                l1.next=ListNode()
            
            l1.next.val = l1.next.val+advance

        result.next=self.addTwoNumbers(l1.next,l2.next)
        return result 
# @lc code=end

