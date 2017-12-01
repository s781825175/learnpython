class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        for i in range(len(asteroids)):
            if i == len(asteroids)-1:
                break
            if asteroids[i] > 0 and asteroids[i+1] < 0:
                if abs(asteroids[i]) < abs(asteroids[i+1]):
                    asteroids.pop(i)
                elif abs(asteroids[i]) > abs(asteroids[i+1]):
                    asteroids.pop(i+1)
                else:
                    asteroids.pop(i+1)
                    asteroids.pop(i)
                return self.asteroidCollision(asteroids)
            if asteroids[i] == 0 and asteroids[i+1] < 0:
                asteroids.pop(i)
                return self.asteroidCollision(asteroids)
            if asteroids[i] > 0 and asteroids[i+1] == 0:
                asteroids.pop(i+1)
                return self.asteroidCollision(asteroids)
        return asteroids

if __name__ == '__main__':
    asteroids=[-2, -1, 1, 2]
    print(Solution().asteroidCollision(asteroids))
