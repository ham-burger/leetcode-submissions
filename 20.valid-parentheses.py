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
        start = 0
        while(index < len(s)):
            # ([{のとき
            if s[index] in self.bracketDic:
                index += 1
            else:
                if(start == index):
                    return False
                # indexは閉じカッコの範囲の一番最初
                diff = (index -1) - start
                last = index + diff
                closes = ""
                # 入力されたカッコに対応する閉じカッコを逆順に取得する
                for i in range(index - 1, start -1 , -1):
                    closes += self.bracketDic[s[i]]
                # 取得したカッコに対応する閉じカッコと、閉じカッコがあるであろうの範囲内の文字列を比較
                if closes == s[index : last + 1]:
                    # 検証した範囲の最後のlastの次を次の検証範囲にする
                    index = last + 1
                    start = index
                else:
                    return False
        return index == start
# @lc code=end
