import gmpy2
from gmpy2 import mpz
import random
#bit_count = 64
rand_state = gmpy2.random_state()
p=int(input("Enter p:"))
q=int(input("Enter q:"))
m=int(input("Enter m:"))
#k1=int(input())
k1=q-1
n2=p-1
l=[]
w=1
rand_state=gmpy2.random_state(42)
n1=gmpy2.mul(p, q) #number(n)
p1=gmpy2.mul(k1,n2) #numberphi
e=gmpy2.next_prime(q)
if gmpy2.gcd(e, p1)==1:
  d=gmpy2.invert(e, p1)
  #print("d:",d)
  if gmpy2.t_mod(e*d, p1)==w:
        m1=mpz(m)
        c=gmpy2.powmod(m1,e,n1)
        m2=gmpy2.powmod(c,d,n1)
        print(c)
        print(e)
        print(d)
        print(n1)



#with open("copy.txt", "w") as file:
  #file.write(str(q))
  




