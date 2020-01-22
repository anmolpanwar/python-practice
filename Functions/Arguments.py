import array as ar
x = ar.array('i',[23,2324,32,4,5])
print(x)
print(id(x))

x.append(12687)
x.append(9696512)
x.append(1432)
x.append(12564)
x.append(1243)
x.append(12324)
x.append(12342)
x.append(12234)
x.append(1234)
x.append(1232)
x.append(32412)
x.append(1243)
x.append(12453)

print(x)
print(id(x))

#implies that address of array remains same no matter how you change the array (or any data type)... reverse/append/insert whatever

def func(b):
    print(id(b))
    print(b)

    b=11
    print(b)
    print(id(b))



a=10
func(a)
