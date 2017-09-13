class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        a=price
        b=special
        c=needs
        d=[]
        for j in special:
            e=0
            for i in range(len(price)):
                e+=j[i]*a[i]
            d.append(e-j[-1])
        e=list(range(len(d)))
        dis=list(zip(d,e))
        print(dis)
        f=[]
        for i in b:
            e=[]
            m=0
            for j in range(len(c)):
                if i[j]==0:
                    i[j]=1
                m=c[j]//i[j]
                e.append(m)
            e=min(e)
            f.append(e)
        print(f)
            


if __name__ == '__main__':
    price=[2,3,4]
    special=[[1,1,0,4],[2,2,1,9]]
    needs=[27,18,21]
    print(Solution().shoppingOffers(price,special,needs))
