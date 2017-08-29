import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        b=[]
        s=collections.Counter(s).most_common()
        for i,j in s:
            for _ in range(j):
                b.append(i)
        return ''.join(b)

if __name__ == '__main__':
    s='tree'
    print(Solution().frequencySort(s))

