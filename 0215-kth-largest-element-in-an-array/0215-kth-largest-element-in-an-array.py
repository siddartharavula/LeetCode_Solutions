class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            if nums:
                heapq.heappop(nums)
        return -nums[0]
        