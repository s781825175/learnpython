class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c)<k:
                print(s.split(c))
                return max(self.longestSubstring(t,k) for t in s.split(c))
        return len(s)

if __name__ == '__main__':
    s="ababbc"
    k=2
    print(Solution().longestSubstring(s,k))
