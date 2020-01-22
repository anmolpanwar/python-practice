#keyword argument - argument me value k saath keyword khud likh denge
def function(name, *data):
    print "Name:", name
    print "Data:", data

function("Anmol", 18, 'btech','Ghaziabad')

print
print

def person(name, **data):
    print "Name:", name

    for i,j in data.items():
        print i,":", j

person('Anmol', Age = 21, City = 'Ghaziabad')


n=1
print(n, )
