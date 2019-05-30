p=97
q=193
n=p*q
fi=(p-1)*(q-1)
# fi=18432
# n=18721

def euklides(a,b):
    # ta funkcja liczy NWD, dziala
    if a>b:
        pass
    else:
        tmp=b
        b=a
        a=tmp
    while(b>0):
        newb=a%b
        a=b
        b=newb
    return a

print(euklides(fi,157))
#te liczby sa wzglednie pierwsze, wiec
e=157

# d*157=1mod(18432)
# d*e=1mod(fi)
# y*n=1mod(m)

# 1=fi*x+e*y

def rozszerzony(m,n):
    # dziala
    if m>n:
        a=m
        aprim=n
    else:
        a=n
        aprim=m
    s=1
    sprim=0
    t=0
    tprim=1
    while aprim!=0:
        q=a//aprim
        tmpa=a
        tmpaprim=aprim
        a=aprim
        aprim=tmpa-q*tmpaprim
        tmps=s
        tmpsprim=sprim
        s=sprim
        sprim=tmps-q*tmpsprim
        tmpt=t
        tmptprim=tprim
        t=tprim
        tprim=tmpt-q*tmptprim
    return t

#d=rozszerzony(7,120)

#d*157 % 18432 =1

d=0
for el in range (10000,20000):
    if (el*157)%fi==1:
        d=el
        break

print(d)
#d=17845
# Hanna - 11 01 18 18 01
imie=[11,1,18,18,1]
msg=[]
for el in imie:
    msg.append((el**e)%n)

print(msg)

t=[]
for el in msg:
    t.append((el**d)%n)
print(t)