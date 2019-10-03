class Solution(object):
    def twoSum(self, nums, target):
        idx = 0
        d = {}
        
        for num in nums:
            t = target - num
            if d.get(t) is not None:
                return [d.get(t), idx]
            else:
                d[num] = idx
            idx = idx + 1
