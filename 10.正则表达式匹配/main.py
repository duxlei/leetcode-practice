# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/regular-expression-matching/

分析思路：
1. 将规则字符串p进行解析，由于'*'和'.'两个字符特殊所以叫进行特殊处理，例如现在有个规则字符：a.v*b.*dfs
   解析的结果如下：[a][.][v*][b][.*][dfs]
2. 使用解析出来的规则字符串数组，依次划过目标字符串，进行判断
3. 在判断结束时，如果目标字符串和规则字符串同时结束，说明匹配成功，否则匹配失败
4. 需要注意的是，在解析出来的规则段中，以'*'结束的段是个特殊的，他代表0或者多个，也就是说，以'*'结束的规则端可能不会映射到目标字符串中

【失败了，有待继续思考】

"""

class Solution(object):
	# 解析规则字符串
	def parse_exp(self, p):
		list = []
		arr = []
		cursor = 0
		while cursor < len(p):
			if p[cursor] == '*':
				if len(arr) > 0:
					if len(arr) > 1:
						list.append(''.join(arr[:-1]))
					list.append(arr[-1] + '*')
					arr = []
				elif len(list) > 0 and list[-1] == '.':
					list.pop()
					list.append('.*')
				cursor = cursor + 1
				# a*aa 等价于 a*
				while True:
					if cursor < len(p) and list[-1][0] == p[cursor]:
						cursor = cursor + 1
					else:
						break
			else:
				if p[cursor] == '.':
					if len(arr) > 0:
						list.append(''.join(arr))
						arr = []
					list.append('.')
				else:
					arr.append(p[cursor])
				cursor = cursor + 1
		if len(arr) > 0:
			list.append(''.join(arr))
		return list

	def match_all_next(self, s, exp, remainder):
		if remainder == 0:
			# 没有下一个匹配项了
		while True:
			if len(s) < len(exp):
				return False
			if s[:len(exp)] == exp:
				s = s[len(exp):]
				break
			else:
				s = s[1:]

	def isMatch(self, s, p):
		exp_list = self.parse_exp(p)
		print exp_list
		all = False
		while len(exp_list) > 0:
			exp = exp_list.pop(0)
			if len(s) == 0:
				break
			# 如果规则段最后一个字符不是*.那就直接匹配
			if exp[-1] != '.' and exp[-1] != '*':
				if all:
					s = self.match_all_next(s, exp, len(exp_list))
					all = False
				elif s[:len(exp)] == exp:
					s = s[len(exp):]
				else:
					return False
			elif exp[-1] == '.':
				# 单个.的情况
				s = s[1:]
				all = False
			else:
				# 结尾是*的情况
				# print exp
				pre = exp[0] #前置字符
				if pre != '.':
					while True:
						if len(s) == 0:
							break
						elif s[0] == pre:
							s = s[1:]
							all = False
						elif all:
							s = s[1:]
						else:
							break
				else:
					# 特殊的.*情况
					if len(exp_list) == 0:
						s = []
					else:
						all = True

		if len(s) > 0 or len(exp_list) > 0 or all == True:
			return False
		else:
			return True


if __name__=="__main__":
	print Solution().isMatch('aaaasdfasABC', 'a*aa.*ABC')







