import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        a=[]
        for i in range((len(s)-len(p)+1)):
            for j in list(p):
                if collections.Counter(s[i:i+len(p)])==collections.Counter(p):
                    a.append(i)
        return list(set(a))


s,p="abab","ab"
print(Solution().findAnagrams(s,p))
