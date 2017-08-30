class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        a=sentence.split()
        for i in range(len(a)):
            for j in dict:
                if a[i].find(j)!=-1:
                    a[i]=j
        return ' '.join(a)

if __name__ == '__main__':
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dict, sentence))

