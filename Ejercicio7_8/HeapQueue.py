import heapq

class HeapQueue:
    def push(self,a,x):
        heapq.heappush(a, x)

    def pop(self,a):
        heapq.heappop(a)

    def ify(self,x):
        heapq.heapify(x)

    def union(*iterables, key=None, reverse=False):
        heapq.merge(*iterables, key, reverse)