class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

haystack="sadasdsadscazs"
needle="c"
print(Solution().strStr(haystack, needle))
