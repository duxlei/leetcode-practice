# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/n-queens/
"""

"""
分析：由于每个皇后所在的行、列、对角线都不能再放置皇后，也就意味着每个将要方式的皇后肯定在不同的行不同的列
也就是说，每一个行、列上肯定会有一个皇后，抽象成逻辑：
如果皇后放置(Xi,Yi)点，那么Xn=Xi,Yn=Yi,Xn+Yi=Xi+Yn,Yi-Xn=Yn-Xi
步骤如下：
1. 从第一行开始，选一个点放置皇后，按照规则过滤掉每一个行不可用的位置
2. 如果约到无解的情况，即当前行没有个可以放置皇后的位置，退回到上一行重新选择
3. 如果最后有解，即所有皇后放置完毕，退回到上一行重新选择
4. 直到第一行的所有位置放置的可能遍历一遍后即可指出循环
"""
class Solution(object):
    def __init__(self):
        self.count = 0
        self.list = []
    # 打印棋盘
    def print_pan(self, pan):
        list = []
        for x in pan:
            list.append(''.join(map(lambda el: '.' if type(el) == int else 'Q', x)))
        return list
    # 初始化棋盘
    def init_pan(self, n):
        list = [[0 for col in range(n)] for row in range(n)]
        return list
    # 更新棋盘信息
    def update_pan(self, pan, n, q_pos, is_back = False):
        for row in range(n):
          for col in range(n):
            Xn = row
            Yn = col
            Xi = q_pos[0]
            Yi = q_pos[1]
            if q_pos[0] == row and q_pos[1] == col:
                pan[row][col] = 0 if is_back else 'Q'
            elif pan[row][col] == 'Q':
                continue
            elif q_pos[0] == row or q_pos[1] == col or Xn+Yi == Xi+Yn or Yi-Xn == Yn-Xi:
                pan[row][col] = (pan[row][col] - 1) if is_back else (pan[row][col] + 1)
    # 检查当前行放置皇后的状况
    def check(self, pan, n, Q):
        # 最后一个皇后
        flag = False
        for col in range(n):
            ele = pan[Q][col]
            if ele == 0:
                flag = True
                self.update_pan(pan, n, (Q, col))
                # 有解，如果Q=7为有效解，否则进行下一步
                if Q == (n - 1):
                    self.count = self.count + 1
                    # print self.print_pan(pan)
                    self.list.append(self.print_pan(pan))
                else:
                    self.check(pan, n, Q+1)
                # 回退
                self.update_pan(pan, n, (Q, col), True)
        return flag

    def solveNQueens(self, n):
        pan = self.init_pan(n)
        self.check(pan, n, 0)
        return self.list
        # print u'解的个数：', self.count

if __name__=="__main__":
    Solution().solveNQueens(4)