from typing import List

from HeapQueue import HeapQueue

a = [3, 5, 1, 2, 6, 8, 7]
b = [20,25,60,80,70]
x = HeapQueue()
x.ify(a)
x.push(a,4)
x.pop(a)
x.union([20,25,60,80,70], [1,6,8,10], [2,3,4,5,7,9])
print(a)
print(b)