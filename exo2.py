a=["janvier" , "mars", "mai","juilet","aout","octobre" ,"decembre"]
b=["avril","juin","septembre","novembre"]
c=["fevrier"]
n=int(input("entrer l'année "))
m=input("entrer le mois :")
if n%4==0 and m in c:
    print("fevrier 28 jours")
elif n%4 != 0 and m in c:
    print("fevrier 29 jours")
elif m in a :
    print(m,'31 jours')
elif m in b  :
    print(m,'30 JOURS')
else :
    print("erreur")
 