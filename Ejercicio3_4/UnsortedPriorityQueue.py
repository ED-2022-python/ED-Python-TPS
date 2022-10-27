from typing import Tuple, Any
from UnsortedPriorityQueueAbstract import UnsortedPriorityQueueAbstract

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):

    def __init__(self):
        self._data = [] #inicializamos la cola

    def __len__(self) -> int:
        return len(self._data)

    def is_empty(self) -> bool:
        return self._data == 0 #retorna True si esta vacia osea == 0 caso contrario False.

    def add(self, k: Any, v: Any) -> None:
        self._data.append(k)

        pass

    def min(self) -> Tuple[Any]:
        pass

    def remove_min(self) -> Tuple[Any]:
        pass

