print("## INTRO ##")


premier, *derniers = 1, 2, 3

print(derniers)  # [2, 3]
print(*derniers) # 2 3



def somme2(z, y):
   return z + y

def somme3(x,y,z):
  return x + y + z

def sommeliste(maliste):
  return sum(maliste)

sommeliste([1,2,3]) # 6

def somme_etoile(*meschiffres):
  return sum(meschiffres)

somme_etoile(1,2,3) # 6



print()
print(" Q1 ")

def puiss(nb, liste):
  li = [x**nb for x in liste]
  return li

a1 = puiss(3, [2,6,9])
print(a1)

assert puiss(2, [4,5]) == [16, 25]
print(puiss(2, [4,5]) == [16, 25])

print()
print(" Q2 ")

def puiss_etoile(nb, *autreschiffres):
  li = [x**nb for x in autreschiffres]
  return li

b1 = puiss_etoile(3,2,6,9)
print(b1)

def mafonction(a, b , **options):
  print(a)
  print(b)
  print(options)

mafonction(1,2, z=8)

print()
print(" Q3 ")

b = 1,2
a = 1,2,3
*a,c = 0, *b

print(*a,c)
print(somme3(*a,c))

print()
print("## Traitement formel des paramètres ##")

triplet = {'x': 1, 'y': 2, 'z': 3}
print(somme3(**triplet))

yz = [1,2]
zz = {'z': 3}

print(yz)
print(zz)

print(somme3(*yz, **zz))

print()
print(" Q4 ")


def question4(*anon, **nom):
  print(anon)
  print(nom)
  sommeanon = sum(anon)
  sommenom = sum(nom.values())
  return sommeanon + sommenom



print(question4(1,2,y=5,z=3))
print(question4(a=1, b=2, c=3))
print(question4(1,b=2,c=3))

print()
print("## Fonction internes ##")



