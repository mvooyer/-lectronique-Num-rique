import matplotlib.pyplot as plt


# Question 1

# On prend un etat initial
# ex : (1, 1, 1) et on teste les combinaisons possible (on observe cycle avec 7 possibilites)
# etat interdit (0, 0, 0) -> etat bloquant


# Question 2

N = 3 # nombre d etats
B1 = 1; B2 = 1; B3 = 1 # initie l etat initial (1, 1, 1)
# nombre binaire qui stock les valeurs de B3 à chaque itération
b3 = B3
s = []
A = 2
for i in range(2**N-1):
    D1 = B2 ^B3
    B3 = B2
    B2 = B1
    B1 = D1
    if B3:
        s.append(A)
    else:
        s.append(-A)
    b3 = (b3|B3)<<1
    print(B1, B2, B3)
print(bin(b3))
plt.plot([i for i in range(2**N-1)], s)
plt.title('S(t)')
plt.show()


# Question 4
# vraiment tout pareil, mais pour 4 bascules (N = 4)
