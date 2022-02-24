#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        braket="()"
        result_set={}
        for i in range(n):
            work=set()
            for e in result_set:
                for index in range(len(e)):
                    work.add(e[:index] + braket + e[index:])
            if(i==0):
                work={braket}
            result_set=work
        result=list(result_set)
        result.sort()
        return result

# @lc code=end

