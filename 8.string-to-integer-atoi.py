#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
        # 空文字の除外
        # +か-はそのまま数値の正負に利用kする
        # 数値を検出したら、それ以降の数値以外の文字列は無視する
        # 数値を変換する。数値がない場合は0にする
        # 32bit数値外の値になった場合、範囲内に収まるようにする
        
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        result_str="0"
        s=s.lstrip(" ")
        has_sign=False
        negative=False
        
        for c in s:
            if(not has_sign):
                if(c=="+"):
                    has_sign=True
                    continue
                elif(c=="-"): 
                    has_sign=True
                    negative=True
                    continue

            if(has_sign):
                if(c.isdigit()):
                    result_str=result_str+c
                else:
                    break
            else:
                if(c.isdigit()):
                    has_sign=True
                    result_str=result_str+c
                else:
                    break
            continue

        result=int(result_str)
        if(negative):
            result=result* -1


        max_result=2147483647
        min_result=(max_result * -1)-1
        if(result<min_result):
            result=min_result
        elif(result>max_result):
            result=max_result
        return result
# @lc code=end

