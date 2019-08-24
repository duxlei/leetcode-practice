# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/3sum/
"""

"""
思路：
1.找出所有大于0的数字数组arr_r
2.找出所有不小于0的数字数组arr_l
3.两种情况：
  a.arr_l里两个数，arr_r取一个数
  b.arr_r里两个数，arr_l取一个数
4.去重

"""

class Solution(object):
  def threeSum(self, nums):
    if len(nums) < 3:
      return []
    arr_r = []
    arr_l = []
    set_r = set()
    set_l = set()
    zero = 0
    for el in nums:
      if el == 0:
        zero = zero + 1
      if el > 0:
        arr_r.append(el)
        set_r.add(el)
      else:
        arr_l.append(el)
        set_l.add(el)

    all = []
    exist = set()
    if zero > 2:
      exist.add('000')
      all.append([0,0,0])
    if len(arr_l) > 1:
      for i in xrange(len(arr_l) - 1):
        for j in xrange(i + 1, len(arr_l)):
          sm = arr_l[i] + arr_l[j]
          if -sm in set_r:
            ls = [arr_l[i], arr_l[j], -sm]
            ls.sort()
            key = reduce(lambda x,y:str(x)+str(y), ls)
            if key not in exist:
              exist.add(key)
              all.append([arr_l[i], arr_l[j], -sm])
    if len(arr_r) > 1:
      for i in xrange(len(arr_r) - 1):
        for j in xrange(i + 1, len(arr_r)):
          sm = arr_r[i] + arr_r[j]
          if -sm in set_l:
            ls = [arr_r[i], arr_r[j], -sm]
            ls.sort()
            key = reduce(lambda x,y:str(x)+str(y), ls)
            if key not in exist:
              exist.add(key)
              all.append([arr_r[i], arr_r[j], -sm])
    return all

if __name__ == '__main__':
  # print Solution().threeSum([-1, 0, 1, 2, -1, -4])
  print Solution().threeSum([-1,0,1,0])

