#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
"""
    1 I
    2 II
    3 III
    4 IV
    5 V
    6 VI
    7 VII
    8 VIII
    9 IX
    10 X
    11 XI
"""
class Solution:
    patternInt = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    patternNextRoman = {
        'I': ['V','X'],
        'X': ['L','C'],
        'C': ['D','M'],
    }
    def romanToInt(self, s: str) -> int:
        # 文字列のindexの0から開始する
        result = 0
        i = 0
        while i < len(s):
            n = s[i]
            # 引数の最後の文字の場合は後ろの文字の考慮はしない
            if i + 1 == len(s):
                result += self.patternInt[n]
                break
            nextRoman = s[i + 1]
            # 読み込んだ文字が減算処理対象かチェックする
            if n in self.patternNextRoman:
                nextRomans = self.patternNextRoman[n]
                # 次の文字が減算処理対象かチェックする
                if nextRoman in nextRomans:
                    # 次の文字に対応する値から今の文字に対応する値を引いた値を追加する
                    result += (self.patternInt[nextRoman] - self.patternInt[n])
                    # 次の文字も演算したのでindexを追加でincrement
                    i += 1
                else:
                    result += self.patternInt[n]
            else:
                result += self.patternInt[n]
            i += 1
        return result
# @lc code=end

