#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    bracketDic = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    def isValid(self, s: str) -> bool:
        # 奇数の場合は除外する
        if(len(s) % 2 != 0):
            return False
        index = 0
        list = []
        while(index < len(s)):
            # ([{のとき
            if s[index] in self.bracketDic:
                list.append(s[index])
            else:
                # カッコが来る前に閉じカッコが来るケース
                if(len(list) == 0):
                    return False
                if(s[index] != self.bracketDic[list.pop(-1)]):
                    return False
            index += 1
        return len(list) == 0
# @lc code=end
