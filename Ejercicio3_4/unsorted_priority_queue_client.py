from UnsortedPriorityQueue import UnsortedPriorityQueue

pd = UnsortedPriorityQueue()

pd.add(1, 'A')
pd.add(2, 'B')
pd.add(3, 'C')
pd.add(4, 'D')
pd.add(5, 'F')
pd.add(6, 'G')
print("Cola de Prioridad:")
print(pd)
print()
print("Vacio? ")
print(pd.is_empty())
print()
print("Minimo")
print(pd.min())
print()

print("Remover minimo")
pd.remove_min()
print(pd)
