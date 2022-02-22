#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s

        # 行のデータを内包した配列
        mapping=['']*numRows
        # 初回の制御のために反転させてる
        reverse=True
        mapIndex=0

        for c in s:
            mapping[mapIndex]=mapping[mapIndex]+c
            if(mapIndex==0 or mapIndex==(numRows-1)):
                reverse=not reverse
            if(reverse):
                mapIndex=mapIndex-1
            else:
                mapIndex=mapIndex+1

        result=''
        for bulk in mapping:
            result=result+bulk
        return result
# @lc code=end

