from UnsortedPriorityQueue import UnsortedPriorityQueue

pd = UnsortedPriorityQueue()

pd.add(1, 'A')
pd.add(2, 'B')
pd.add(3, 'p')
pd.add(4, 'C')
pd.add(1233, 'k')
pd.add(295, 'L')

print(pd)
print()
print("Vacio?: ")
print(pd.is_empty())
