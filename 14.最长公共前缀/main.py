# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/longest-common-prefix/
"""

"""
思路：
1. 字符串数据内的元素，两两组合取公共前缀，形成一个新的前缀字符串数组(Set)
2. 然后递归
3. 直到最后数组的长度为1

["flower","flowyx","flight"]


["abc", "abd", "abc"]
["ab", "abc", 'ab']

"""

class Solution(object):
  def longestCommonPrefix(self, strs):
    if len(strs) < 2:
      return strs[0] if bool(strs) else ''
    sets = set()
    for i in xrange(len(strs) - 1):
      for j in xrange(i + 1, len(strs)):
        le = min(len(strs[i]), strs[j])
        if le < 1:
          sets.add('')
          continue
        temp = ''
        for x in xrange(le):
          if strs[i][:x+1] == strs[j][:x+1]:
            temp = strs[i][:x+1]
          else:
            break  
        sets.add(temp)
    return self.longestCommonPrefix(list(sets))

if __name__ == '__main__':
  # print Solution().longestCommonPrefix(["flower","flowyx","flight"])
  print Solution().longestCommonPrefix(["dog","racecar","car"])