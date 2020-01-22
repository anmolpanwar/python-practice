class student:
    college = "UPES"                        #static variable
    loc = "Dehradun"
    count=1

    def __init__(self,name,branch,sapid):
        self.name = name
        self.branch = branch
        self.sapid = sapid
        self.display()
        print "id",id(self)
        print

    @staticmethod
    def collegename():
        print "Students of " + student.college

    @classmethod                             #method to access static variable
    def location(cls):
        print cls.loc

    def display(self):
        print student.count
        print self.name + "\t\t" + self.branch + "\t\t" ,self.sapid
        student.count+=1                     #access class variable ALWAYS BY CLASS NAME


student.location()
student.collegename()
print

s1 = student("ANMOL", "CS", 52999)

s2 = student("AISH", "CS", 52251)

s3 = student("AMAN", "CS", 52700)

s4 = s3                                     #PASS BY REFERENCE (DONO KI ID SAME) (same baloon with 2 threads)
print "When we say they are equal, S4 ki id same as s3: " , id(s4)

s4.name = "NOT AMAN"

print "S3 name is now -", s3.name          #color of baloon tied to thread 1 is changed, thread 2 is tied to same baloon
print                                      #suffers the same effect. Its baloon colour also changes

s4 = student("Vishal", "OOS", 324235)

print "When we define s4 with its own values (or even same values), ID changes: ", id(s4)
print                                     #when we define an object its own values, WE TIE THE THREAD TO ANOTHER BALOON!
s4.name = "NOT VISHAL"

print "Name of s4 changed to", s4.name

print "ID of s4 is -", id(s4), '----- SAME!!!!'   #changing values of an object does not affect its address. OBJECTS ARE MUTABLE

print
stunamelist = [s1.name,s2.name,s3.name]

print "Names: ", stunamelist
print
print student.count-1, "records yet."
