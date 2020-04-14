from base.Long10 import Long10 as l10
from base.Cpy32 import Cpy32 as cp
from base.CreateBA import CreateBA as cb
from base.Sqrt import Sqrt as sq

a = bytearray()
b = bytearray()

for i in range(32):
    a.append(0)

for i in range(32):
    b.append(i)


print("prima a",a)
print("prima b",b)

c = '5e384a3c2b54ee93ba71ea50919bb2f7b55acc681fc7698c4a64345faa07994d'
cp(a,b)


d = bytearray.fromhex(c)

print(d)

print("dopo a",a)
print("dopo b",b)

l = l10(0,0,0,0,0,0,0,0,0,0)
m = l10(1,2,3,4,5,6,7,8,9,10)

w = sq(l,m)

#print(due.printAll())

