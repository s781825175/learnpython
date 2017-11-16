class Solution(object):
    def zhishu(self, target):
        """
        :type target: int
        :rtype: List[int]
        """
        a=list(range(2,target+1))
        b,c=[],[]
        for i in a:
            if i not in c:
                b.append(i)
                for j in range(2,int(target/i+1)):
                    c.append(i*j)
        return b

if __name__ == '__main__':
    target=100
    print(Solution().zhishu(target))

        
