class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        a = []
        for i in range(len(s)-10):
            if s[i:i+10] in s[:i] or s[i:i+10] in s[i+10:]:
                a.append(s[i:i+10])
        a=list(set(a))
        return a

if __name__ == '__main__':
    s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))
