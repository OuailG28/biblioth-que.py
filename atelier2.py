 #exercice 1

#a=int(input("entrer un nombre : "))
 #for i in range(1,11) :
    # print(a,"x",i,"=",a*i)

#exercice 2

#a=int(input("entrer un nombre positive : "))
#s=0
#for i in range(1,a+1):
 #       s=s+i
#print(s) 

#exercice 3

#for i in range(0,10,2):
 #    print(i*i)
# exercice 4
# while True:
     
   #   mot=input("entrer un mot ou une phrase : ")
   #   print(mot)
   #   if mot=="fin":
   #      print("fin de programe")
   #      break

max = 0
while True:
    a = int(input("entrer un nombre : "))
    if a != 0 and max < a:
      max = a
    if a == 0:
       print(max)
       break
    