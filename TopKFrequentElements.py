import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return list(zip(*collections.Counter(nums).most_common(k)))[0]

if __name__ == '__main__':
    nums=[1,1,1,2,2,3]
    k=2
    print(Solution().topKFrequent(nums,k))
            
        
