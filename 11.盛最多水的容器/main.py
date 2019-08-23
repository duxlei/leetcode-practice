# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/container-with-most-water/

思路1：暴力
计算每个元素的做大面积，最后比较保留面积

思路2：双指针
1.假设有两个指针分别指向头和尾
2.每次将较短一侧的指针向较长的一端移动
3.直到两个指针相遇，结束

"""

class Solution:
  # 思路1
  def maxArea_1(self, arr):
    if len(arr) == 2:
      return min(arr)
    mx = 0
    for i in xrange(1,len(arr)):
      mx = max(min(arr[0], arr[i]) * i, mx)
    return max(mx, self.maxArea(arr[1:]))

  def maxArea_2(self, arr):
    if len(arr) == 2:
      return min(arr)
    mx = 0
    while True:
      if len(arr) == 2:
        mx = max(min(arr), mx)
        break
      mx = max(mx, min(arr[0], arr[-1]) * (len(arr) - 1)) 
      if arr[0] >= arr[-1]:
        arr.pop()
      else:
        arr.pop(0)
    return mx

if __name__=="__main__":
  # print Solution().maxArea_1([1,8,6,2,5,4,8,3,7])
  # print Solution().maxArea_2([1,8,6,2,5,4,8,3,7])
  print Solution().maxArea_2([1,3,2,5,25,24,5])