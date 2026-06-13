class Solution:
    def minOperations(self, nums, k) :
        total = 0
        for x in nums:
            total += x
        return total % k
