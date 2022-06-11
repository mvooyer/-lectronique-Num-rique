# Question 1:
for i in [0, 1]:
    for j in [0, 1]:
        for k in [0, 1]:
            for l in [0, 1]:
                print(i, '^', j, '^', k, '^', l, ' = ', i ^ j ^ k ^ l)

# La sortie donne 1 si il y a un nombre d’entrees impairs qui valent 1.
# Inversement, la sortie donne 0 si il y a un nombre d’entrées pairs qui valent 0.


# Question 2 :

# valeur initiale de x
x = 0
# nombre d iterations
N = 10
print('x initial =', x)
for i in range(N):
    x ^= 1
    print(x)

# un nombre impair d operation change un 0 en 1 et un nombre pair change un 1 en 0


# Question 3 :

# il faut 7 bits pour representer le nombre 117
def representation(y):
    print('Nombre x (base de 10) =', y)
    print('Base de 2', bin(y))
    print('Bade de 16', hex(y))
    print(f'Il faut {len(bin(y))-2} bits pour stocker le nombre {y} \n')


representation(117)
representation(1101)
representation(43605)
representation(3735928559)


# Question 4 : Application et explication des registres a decalage

# methode 1
a = 117
mask = 1 << 6 # on genere un nombre binaire de la meme taille qui commence par 1 suivi de n zeros
while(mask):
    print(int((mask & a) != 0), end='')
    mask >>= 1

# methode 2
a = 117
while(x): # plus simple mais donne la decomposition binaire a l envers (a lire de droite a gauche)
    print(x & 1, end='')
    x >>= 1
print()

# Question 5

# a)
# sur 7 bits le nombre le plus grand que l on peut stocker est 127

# b)
# parite paire (renvoie 0 si le nombre de 1 est paire et 0 si impaire)
def parite_paire(n):
    p = 0
    mask = 1 << 6
    while(mask):
        p ^= int((mask & n) != 0)
        mask >>= 1
    return p


x = 117
print(parite_paire(x))

# c)
y = (parite_paire(x) << 8) | x # y est le nombre x avec a gauche la parite paire

# d)
# on fait pareil mais avec la fonction parite impaire
def parite_impaire(n):
    p = 1
    mask = 1 << 6
    while(mask):
        p ^= int((mask & n) != 0)
        mask >>= 1
    return p


# Question 6

msg = ['1', '0', '0', '0', '0', '1', '0']
cle = ['1', '1', '1', '0', '0', '1', '0']

def crypt(key, message):
    output = [str(int(message[i]) ^ int(key[i]))for i in range(len(message))]
    return output

# affiche le message a crypter
print(msg)
# affiche le message crypte
print(crypt(cle, msg))
# affiche le message decrypte (identique au message avant cryptage)
print(crypt(cle, crypt(cle, msg)))

def transform_int(message):
    entier = 0
    for i in range(len(message)):
        entier += 2**i * int(message[-i-1])
    return entier


# affiche le message converti en nombre entier
print(transform_int(msg))

def caractere(message):
    cara = chr(transform_int(message))
    return cara

# affiche le caractere contenu dans le message
print(caractere(msg))

# les caracteres cryptes avec la cle donnee plus tot
c1 = '0111010'
c2 = '0010111'
c3 = '0011110'
c4 = '0011110'
c5 = '0011101'
# decrypte avec la meme cle et converti en caractere
print(caractere(crypt(cle, c1)), end='')
print(caractere(crypt(cle, c2)), end='')
print(caractere(crypt(cle, c3)), end='')
print(caractere(crypt(cle, c4)), end='')
print(caractere(crypt(cle, c5)), end='')

# si les nombres sont au format hexadecimal
# de type msg = 0x72 et cle = 0x3A, il suffit de faire chr(cle^msg)
# pour afficher le caractere (-> plus simple)