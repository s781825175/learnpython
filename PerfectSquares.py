class Solution:
    def numSquares(self, n):
        if n < 2:
            return n
        lis = []
        i = 1
        while i * i <= n:
            lis.append( i * i )
            i += 1
        a = 0
        b = {n}
        while b:
            a += 1
            temp = set()
            for x in b:
                for y in lis:
                    if x == y:
                        return a
                    if x < y:
                        break
                    temp.add(x-y)
            b = temp

        return a

if __name__ == '__main__':
    n=12
    print(Solution().numSquares(n))
