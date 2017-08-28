class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=0
        for i in range(len(s)):
            for j in range(len(s),0,-1):
                if s[i:j]==s[i:j][::-1]:
                    n+=1
                if i+1==j:
                    break
        return n

if __name__ == '__main__':
    s="aaa"
    print(Solution().countSubstrings(s))
