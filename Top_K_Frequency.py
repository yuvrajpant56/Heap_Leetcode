import heapq
from collections import Counter


def topKFrequent(nums, k):
    # Step 1: Count frequencies 
    freq = Counter(nums)
    # Step 2: Use a heap to find the k most frequent element
    heap=[]
    # Step 3: Push elements into the heap
    for num, count in freq.items():
        heapq.heappush(heap, (count, num))
        # If the heap exceeds size k, pop the smallest element
        if len(heap) > k:
            heapq.heappop(heap)
    # Step 4: Extract the elements from the heap
    return [num for count, num in heap] 
# Example usage
nums = [1, 1, 1, 2, 2, 3]
answer=topKFrequent(nums, 2)  # Example usage
print(answer)  # Output: [1, 2]