t1 = (1233, 245145)
t2 = (4, 6, 9, 4)
print(t1[1])
print(t2[2])
#t1[1] = 21 it is not possible in tuples to add the new elemets
t3 = t2[1:3]
print(t3)

print('----------')
l4 = [123, 456, 3456, 12, 345, 987, 99, 55]
print(l4)
s1 = set(l4)
print(s1)
#not possible to address an element of a set
#print(s1[3])
for el in s1:
    print(el)

s2 = set(l4)
print(s2)



