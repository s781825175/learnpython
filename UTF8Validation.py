class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        bi=[]
        for i in data:
            if len(str(bin(i))) != 10:
                bi.append('2')
            else:
                if list(str(bin(i)))[2:4] == ['1','0']:
                    bi.append('1')
                else:
                    bi.append(bin(i))
        for i in range(len(bi)):
            if len(bi[i]) == 10:
                for j in range(2,10):
                    if bi[i][j] == '0':
                        b=j-3
                        break
                if bi[i+1:i+b+1] != ['1'] * b:
                    return False
        return True



if __name__ == '__main__':
    data = [197,130,1]
    print(Solution().validUtf8(data))
