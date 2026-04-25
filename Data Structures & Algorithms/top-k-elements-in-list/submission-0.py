class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Nos = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, count in Nos.items():
            bucket[count].append(num)

        lists = []

        for i in range(len(bucket)-1, 0 , -1):
            for num in bucket[i]:
                lists.append(num)
                if len(lists) == k:
                    return lists
        