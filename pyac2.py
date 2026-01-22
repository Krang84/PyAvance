seq1 = ['a','b','c']
seq2= [1,2,3]
listi = [(lettre, nombre) for lettre in seq1 for nombre in seq2]
print(listi)
[('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]


