class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        reset=list()
        list1, list2, list3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        for i in range(len(words)):
            l=words[i]
            a=list((l.lower()))
            b=set(a)
            if b.issubset(list1) or b.issubset(list2) or b.issubset(list3):
                reset.append(l)
        return reset

x=Solution()
words=["Hello", "Alaska", "Dad", "Peace"]
reset=x.findWords(words)
print(reset)
