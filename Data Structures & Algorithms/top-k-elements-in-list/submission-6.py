from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[]]*(len(nums)+1)
        output = []
        current_k = 0

        for num, count in counter.items():
            # print(count, num)
            if not buckets[count]:
                buckets[count] = [num]
            else:
                buckets[count].append(num)

        # for i, bucket in enumerate(reversed(buckets)):
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i] and current_k<k:
                output.extend(buckets[i])
                current_k += 1

        # most_comm = counter.most_common(k)
        # output = [num for num, count in counter]
        return output[:k]