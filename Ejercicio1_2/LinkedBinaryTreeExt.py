from typing import Any, List
from Ejercicio1_2.LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from python_ed_fcad_uner.data_structures import LinkedBinaryTree, BinaryTreeNode

class LinkedBinaryTreeExt(LinkedBinaryTree,LinkedBinaryTreeExtAbstract):
    def hermanos(self, nodo1 : BinaryTreeNode, nodo2: BinaryTreeNode) -> bool: 
        # si son hijo izquierdo e hijo derecho del mismo nodo padre
        #Si el nodo que vamos a insertar nodo1 cual es su padre?
        #nodo 2 cual es su padre? 
        #si los padres son == entonces 👌 hermanos
        # si son equals? no son hermanos.


        
        pass

    def hojas(self) -> List[Any]:
        # un nodo es hoja cuando no tiene hijos. no es padre
        #

        pass
    def internos(self) -> List[Any]:
        #Si tiene 2 hijos es un nodo interno.
        #verificar que sea padre y tengo hijos y 2.
        pass

    
    def profundidad(self, nodo : BinaryTreeNode) -> int:

        
        pass
    def altura(self, nodo : BinaryTreeNode) -> int:
        pass

