import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        return max(min(abs(house - heater)
                       for i in [bisect.bisect(heaters, house)]
                       for heater in heaters[i-(i>0):i+1])
                   for house in houses)
        

houses=[1,2,3,4,5]
heaters=[2]
print(Solution().findRadius(houses, heaters))
if __name__ == '__findRadius__':
    findRadius()
