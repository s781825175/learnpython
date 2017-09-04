class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=0
        for i in s:
            a=t.find(i,a)
            if a == -1:
                return False
        return True


if __name__ == '__main__':
    s,t = "axc", "ahbgdc"
    print(Solution().isSubsequence(s,t))
