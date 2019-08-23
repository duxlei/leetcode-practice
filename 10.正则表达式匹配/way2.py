# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/regular-expression-matching/

采用递归回溯的方式：
1. 如果无*，且第一个位置匹配成功则，则递归匹配(s[1:], p[1:])
2. 如果有*，则第一个位置匹配且(s[1:], p)递归成功 或者 (s, p[2:])递归成功

"""

class Solution(object):

  def isMatch(self, s, p):
    if not p:
      return not s

    first_match = bool(s) and (p[0] == '.' or p[0] == s[0])
    ast = p[1] == '*' if len(p) > 1 else False
    print s, p, first_match, ast
    if not ast:
      return first_match and self.isMatch(s[1:], p[1:])
    else:
      return (first_match and self.isMatch(s[1:], p)) or self.isMatch(s, p[2:])


if __name__=="__main__":
  print Solution().isMatch('aab', 'c*a*b')







