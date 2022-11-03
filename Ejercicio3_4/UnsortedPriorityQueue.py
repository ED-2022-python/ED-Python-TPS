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
        """ Devuelve una tupla conformada por la clave(K)y valor(V) del ítem con menor valor de
               clave.
               Raises:
               Exception: Arroja excepción si se invoca cuando la estructura está vacía.
               Returns:
               Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
               """
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
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


