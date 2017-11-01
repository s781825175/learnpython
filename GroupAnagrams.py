class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a=[]
        b=[]
        c=[]
        for i in strs:
            a.append(list(i))
        a=list(map(sorted,a))
        for i in range(len(a)):
            a[i].append(i)
            a[i]=a[i][::-1]
        a=sorted(a,key=lambda a:a[2])
        for i in range(len(a)-1):
            b.append(a[i][0])
            if a[i][1:] != a[i+1][1:]:
                c.append(b)
                b=[]
            if i==len(a)-2:
                if a[-1][1:]==a[-2][1:]:
                    b.append(a[-1][0])
                    c.append(b)
                else:
                    c.append(list(a[-1]))
        b=[]
        for i in c:
            a=[]
            for j in i:
                a.append(strs[j])
            b.append(a)
        return b


if __name__ == '__main__':
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
