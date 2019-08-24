# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/roman-to-integer/
"""

"""
思路：
罗马字符串和罗马字母表进行头部匹配，如果匹配上了，罗马字符串移除头部元素，否则罗马字母表移除头部元素（罗马字母表从大到小排列）
每次匹配上就将罗马字母表对应的整数累加
知道罗马字符串和罗马字母表其中一个为空则停止，返回累加整数

对应
1:    I
4:    IV
5:    V
9:    IX
10:   X
40:   XL
50:   L
90:   XC
100:  C
400:  CD
500:  D
900:  CM
1000: M


例如：CXXIII
100 + 10 + 10 + 3 = 123
例如：CXXIX
100 + 10 + 10 + 9 = 129
"""

class Solution(object):
  def romanToInt(self, s):
    ls = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    mp = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    num = 0
    while True:
      if not bool(s) or not bool(ls):
        break
      if s[0] == ls[0]:
        num = num + mp[ls[0]]
        s = s[1:]
      elif s[:2] == ls[0]:
        num = num + mp[ls[0]]
        s = s[2:]
      else:
        ls.pop(0)
    return num

if __name__ == '__main__':
  print Solution().romanToInt('MCMXCIV')