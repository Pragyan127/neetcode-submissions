class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = Counter(nums)
        emptys = [[] for _ in range(len(nums)+1)]

        for val, count in bucket.items():
            emptys[count].append(val)

        lists = []
        for i in range(len(emptys)-1, 0 , -1):
            for num in emptys[i]:
                lists.append(num)
            if len(lists) == k:
                return lists