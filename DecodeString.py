import re
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s
if __name__ == '__main__':
    s = "3[a2[e]cf]"
    print(Solution().decodeString(s))
