
def Maximum(i):
    if len(i)>2:
        y = Maximum(i[0:len(i) // 2])
        print(y)
        x = Maximum(i[len(i) // 2:len(i)])
        print(x)
        if y < x:
            return x
        else:
            return y
    if len(i)==2:
        if i[0]>i[1]:
            return i[0]
        else:
            return i[1]
    if len(i)<2:
        return i[0]
from random import randint
a=[randint(0,9) for d in range(5)]
print("Przykład 1 lista to ", a, "jej największy element ", Maximum(a))
b=[randint(0,9) for o in range(8)]
print("Przykład 2 lista to ", b, "jej największy element", Maximum(b))
c=[randint(0,9) for w in range(10)]
print("Przykład 3 lista to ", c, "jej największy element", Maximum(c))