from typing import Any, List
from LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from python_ed_fcad_uner.data_structures import LinkedBinaryTree, BinaryTreeNode, LinkedQueue


class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def hermanos(self, nodo1 : BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        return self._search_parent(nodo1).__eq__(self._search_parent(nodo2))

    def hojas(self) -> List[Any]:
        queue = LinkedQueue()
        queue.enqueue(self._root)
        nodos_hoja = []
        while not queue.is_empty():
            current = queue.first()

            if current.children_count() == 0:
                nodos_hoja.append(current.element)

            if current.left_child:
                queue.enqueue(current.left_child)

            if current.right_child:
                queue.enqueue(current.right_child)

            queue.dequeue()
        return nodos_hoja

    def internos(self) -> List[Any]:
        queue = LinkedQueue()
        queue.enqueue(self._root)
        nodos_hoja = []
        while not queue.is_empty():
            current = queue.first()

            if current.children_count() > 0 and self._search_parent(current) is not None:
                nodos_hoja.append(current.element)

            if current.left_child:
                queue.enqueue(current.left_child)

            if current.right_child:
                queue.enqueue(current.right_child)

            queue.dequeue()
        return nodos_hoja

    def profundidad(self, nodo : BinaryTreeNode) -> int:
        nivel=0
        while self._search_parent(nodo) != None:
            nivel += 1
            nodo = self._search_parent(nodo)
        return nivel
    def altura(self, nodo : BinaryTreeNode) -> int:
        if nodo.right_child == None and nodo.left_child == None:
            return 0
        else:
            x = -1
            y = -1
            if nodo.left_child != None:
                x = self.altura(nodo.left_child)
            if nodo.right_child != None:
                y = self.altura(nodo.right_child)
            return 1 + max(x,y)