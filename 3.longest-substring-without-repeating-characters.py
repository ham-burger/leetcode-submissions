#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        previous=""
        result=0
        for c in s:
            if(c in previous):
                index=previous.find(c)+1
                previous=previous[index:]+c
            else:
                previous=previous+c
                result=max(len(previous),result)

        return result
# @lc code=end