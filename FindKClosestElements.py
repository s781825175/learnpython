class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        diff=[]
        dex=[]
        for i in arr:
            a=i-x
            diff.append(abs(a))
        b=range(len(diff))
        dexx=list(zip(diff,b))
        dexx.sort()
        dex=[]
        for i in range(k):
            dex.append(dexx[i])
        diff=[]
        for i in dex:
            diff.append(arr[i[1]])
        return diff



if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k=4
    x=3
    print(Solution().findClosestElements(arr,k,x))
