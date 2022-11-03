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
        return len(self.queue) == 0#retorna True si esta vacia osea == 0 caso contrario False.

    def add(self, k: Any, v: Any) -> None:
        self.queue.append((k, v)) # _Item es la clase definida en PriorityQueueBase
        #        self._upheap(len(self.queue) - 1)  #El nuevo nodo es hoja y hay que dejarlo ordenado.

    def min(self) -> Tuple[Any]:
        pass

    def remove_min(self) -> Tuple[Any]:
        pass

