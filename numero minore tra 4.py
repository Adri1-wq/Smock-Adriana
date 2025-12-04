#dati 4 numeri in ingresso resituire il minore di 4

def minore(a,b,c,d):
 min = 0  
 if a<b:
      if a<c:
        if a<d:
            min = a
        else:
            min = d
      else:
        if c<d:
            min = c
        else: 
            min = d
 else:
     if b<c:
        if b<d:
            min = b
 return min

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))

m = minore(a,b,c,d)
print ("tra ", a,",",b, ",",c,"e",d, " il minore è ",m)
