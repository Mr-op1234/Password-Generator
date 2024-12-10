from decimal import Decimal, getcontext
getcontext().prec = 100 
n = (input("Enter a name or a number: ")).upper()
n = ''.join(n.split())
l = len(n)
k = 0
if ord(n[0])>=65 and ord(n[0])<=90:
    k = 1
    for i in n:
        n = n+str(ord(i))
    n = n[l:]
    l = len(n)
n = Decimal('0.' + n)
res = ""
name = input("Enter name where you are creating account ")
name = ''.join(name.split())
iterations = l  + len(name)

for i in range(iterations):
    n = n * 16  
    integer_part = int(n) 
    st = hex(integer_part)[2:]
    
    res = res+ st
    n -= integer_part  
res = "Your Password is " +res
print(res)
