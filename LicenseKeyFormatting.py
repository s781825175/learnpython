class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S=S.upper()
        S=S.replace('-','')[::-1]
        for i in S[K-1::K]:
            S=S.replace(i,i+'-')
        S=S[::-1]
        if S.startswith('-')==1:
            return S.replace('-','',1)
        return S

if __name__ == '__main__':
    S='2-4A0r7-4k'
    K=3
    print(Solution().licenseKeyFormatting(S,K))
