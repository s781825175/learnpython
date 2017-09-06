import collections
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a=collections.Counter(moves)
        return (a['U']==a['D'] and a['L']==a['R'])

if __name__ == '__main__':
    moves='LLDDRRUU'
    print(Solution().judgeCircle(moves))
