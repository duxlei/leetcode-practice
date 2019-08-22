"""
https://leetcode-cn.com/problems/regular-expression-matching/
"""

class Solution(object):
	def isMatch(self, s, p):
	    for x in xrange(0,len(p)):
	    	# if p[x] == "."
	    	print(x, p[x])

	    sl = list(s)
	    sl.reverse()
	    while len(sl) > 0:
	    	print(sl.pop())
	    print(sl)

	    idx_s_l = idx_s = 0
	    idx_p_l = idx_p = 0
	    while len(s) < idx_s || len(p) < idx_p:
	    	if p[idx_p] == '.':
	    		if p[idx_p_l] == '*':
	    			
	    	if s[idx_s] == p[idx_p]:
	    		idx_s++
	    		idx_p++ 

	    	pass

	    return False;


if __name__=="__main__":
	Solution().isMatch('123', 'abc')