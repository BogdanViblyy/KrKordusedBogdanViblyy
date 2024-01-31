#1

osaüks=" (\_/) "
osakaks=" (o o) "
osakolm="/ | \* "

try:
    n=int(input("Siseta arv 1-9"))
    if 1<=n<=9:
        print(osaüks*n)
        print(osakaks*n)
        print(osakolm*n)
    else:   
        print("valed andmed")
except:
    print("valed andmed")



#2





print=sum(range(0,14,1))




#3

import random
x=random.randint(1,100)
katse=int(0)
print("Proovi ära arvata, sa saad proovida 10 korda!")
while katse<=10:
    katse+=1
    i=int(input("Mis numbri ma välja mõtlesin?"))
    if i==x:
        print("Sina arvasid ära!")
        break
    elif i!=x:
        int(katse+1)
        if i<x:
            print("Liiga väike arv, proovi uuesti.")
        else:
            print("Liiga suur arv, proovi uuesti.")
else:
    print("Sinu katsed on läbi.")

    



#5
try:
    arv=int(input("sisseta täisarv"))
    summa=0
    korrutis=1
    while arv/10>=1:
        n=arv%10
        summa=summa + n
        korrutis=korrutis * n
        arv=arv//10
    print("Numbrite summa selles arvus on",summa)
    print("Numbrite korrutis selles arvus on",korrutis)
except:
    print("valed andmed")






#4

try:
    arv=int(input("Sisseta täisarv: "))
    ümberpööratud= 0
 
    while arv > 0:
        n=arv%10
        arv=arv//10
 
        ümberpööratud=ümberpööratud*10
        ümberpööratud = n2 + digit
 
 
    print("See sama arv ümberpööratud:", ümberpööratud)
except:
    print("valed andmed")
