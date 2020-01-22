#OPERATOR OVERLOADED


a='abc'
b='xyz'

print(str.__add__(a,b)) #str class k objects ko add karne k liye ye "__add__" method hota hai. Ye method call tab hota hai silently jab hum "+" operator likhte hain.
print(a+b)
a=67
b=9

print(int.__add__(a,b)) # aur aisa hi method int me bhi hota hai jisse integers add karte hain. Already "__add__" naam ka ye method overloaded hai
print(a+b)              #strings ko concatenate karta hai aur integers ko add karta hai

class student:         #apni khud ki class banake uske objects k through iss method ko (ya kisi aur operator k method ko) overload kar sakte hain apne hisaab se.

    def marks(self,maths, phy, chem):
        self.maths = maths
        self.phy = phy
        self.chem = chem

    def __add__(self,other):                #iss method me hum ne marks plus kar diye jo bhi student k objects banenge unke marks plus ho jaenge jab objects ko plus karenge
        maths = self.maths + other.maths
        phy = self.phy + other.maths
        chem = self.chem + other.chem

        s3 = student()
        s3.maths = maths
        s3.phy = phy
        s3.chem = chem

        return s3

s1 = student()
s1.marks(8,7,9)
s2 = student()
s2.marks(8,5,7)

s3 = s1+s2                  #this statement would have given an error if "__add__" had not been defined in the class.

print s3.maths


print type(s3)
print s3                #address of s3 instance  printed


"""Or instead of creating a new instance 's3' in add method itself and assigning its values there and then, we can also just  return the values of
    maths, phy, chem and create a new object outside the class as usual and store those values in respective s3 attributes"""
