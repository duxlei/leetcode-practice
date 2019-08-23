# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/integer-to-roman/
"""

"""
思路：
关键在于将整数分解成：1、【4】、5、【9】、10、【40】、50、【90】、100、【400】、500、【900】、1000之和的形式
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


例如：123
100 + 10 + 9 + 4 = CXIXIV
100 + 10 + 10 + 3 = CXXIII
例如：129
100 + 10 + 10 + 9 = CXXIX
"""

class Solution(object):
  def intToRoman(self, num):
    ls = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    mp = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    str = []
    for n in ls:
      if num < n:
        continue
      str.append(''.join([mp[n] for i in range(num / n)]))
      num = num % n
    return ''.join(str)

if __name__ == '__main__':
  print Solution().intToRoman(3)