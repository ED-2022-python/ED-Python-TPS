from typing import Tuple, Any
from python_ed_fcad_uner.data_structures.priority_queues import PriorityQueueBase
from UnsortedPriorityQueueAbstract import UnsortedPriorityQueueAbstract

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract,PriorityQueueBase):
    def __init__(self):
        self.queue = list()

    def __len__(self) -> int:
        return len(self.queue)

    def __repr__(self) -> str:
        if self.is_empty():
            return "ArrayHeap()"

        return f"({', ' .join(list(str(x) for x in self.queue))})"

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def add(self, k: Any, v: Any) -> None:
        self.queue.append((k, v))

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("Heap vacío. No se puede continuar.")

        min = 0
        for i in range(len(self.queue)):
            if self.queue[i] < self.queue[min]:
                min = i
        item = self.queue[min]
        del self.queue[min]
        return item

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("Priority queue is empty.")

        self.intercambio(0, len(self.queue) - 1)  # Pone el mínimo valor al final de la lista.
        item = self.queue.pop()  # Quita el valor final de la lista.

        return (item)

    def intercambio(self, i:int, j:int)-> None:
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
