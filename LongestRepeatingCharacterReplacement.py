#允许k次错误的最大连续相同字符串
import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = lo = 0
        counts = collections.Counter()
        for hi in range(len(s)):
            counts[s[hi]] += 1
            max_char_n = counts.most_common(1)[0][1]
            if hi - lo - max_char_n + 1 > k:
                counts[s[lo]] -= 1
                lo += 1
        return hi - lo + 1


if __name__ == '__main__':
    s='ACABABCBA'
    k=1
    print(Solution().characterReplacement(s,k))
