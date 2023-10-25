# Exo5
n = int(input("Entrez un nombre entier : "))
 
resultat = 1
 
for i in range(1, n+1):
    resultat *= i
 
print("Le factoriel de", n, "est", resultat)