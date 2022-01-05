#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 解答1
        # -の場合に早期return
        if x < 0:
         return False
        # 入力を文字列に変換
        strX = str(x)
        # 文字列の長さを取得する
        size = len(strX)
        # 長さ/2を切り捨てて、それを計算対象のindexとする
        endIndex = size // 2
        # 最初からindexまで、+と-でアクセスする
        for c in range(endIndex):
            if strX[c] != strX[-(c+1)]:
                return False
        return True
        # アクセスした結果が最後まで同じ文字だった場合はtrue

# @lc code=end

