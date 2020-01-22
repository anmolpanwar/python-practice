print ("____Tic-Tac-Toe____\n\n")

des = [["     ",'     ','     '],["     ",'     ','     '],["     ",'     ','    ']]
struct = [['|','|','\n'],['|','|','\n'],['|','|','\n']]
postion = [0,"     ","     ","     ","     ","     ","     ","     ","     ","     "]
count = 0
def userdes():
    global count
    pos = int(input("\n\nEnter the position for your X: "))
    if pos ==1:
        des[0][0]="  X  "
    elif pos ==2:
        des[0][1]="  X  "
    elif pos==3:
        des[0][2]="  X  "
    elif pos==4:
        des[1][0]="  X  "
    elif pos==5:
        des[1][1]="  X  "
    elif pos==6:
        des[1][2]="  X  "
    elif pos==7:
        des[2][0]="  X  "
    elif pos==8:
        des[2][1]="  X  "
    else:
        des[2][2]="  X  "
    count+=1
    printdes()

def macdes(pos):
    global count
    if pos ==1:
        des[0][0]= "  O  "
    elif pos ==2:
        des[0][1]= "  O  "
    elif pos==3:
        des[0][2]= "  O  "
    elif pos==4:
        des[1][0]= "  O  "
    elif pos==5:
        des[1][1]= "  O  "
    elif pos==6:
        des[1][2]= "  O  "
    elif pos==7:
        des[2][0]= "  O  "
    elif pos==8:
        des[2][1]= "  O  "
    else:
        des[2][2]= "  O  "
    count+=1
    printdes()


def make():
    if ifspace():
        danger = checkopp()
        macdes(danger)
    else:
        return


def checkopp():
    if des[0][0]=='  O  ' and des[0][1]=='  O  ':
        pass


def printdes ():
    for i in range(3):
        a,b,flag=0,0,1
        for j in range(6):
            if flag==1:
                print (des[i][a], end = "")
                a+=1
                flag=0
            else:
                print(struct[i][b], end = "")
                b+=1
                flag=1
        if i!=2:
            print('_________________')
    print ('\n')

def ifspace():
    for i in range(3):
        for j in range(3):
            if des[i][j]=="     ":
                return True
            else:
                return False

def main():

    printdes()
    userdes()
    make()
if __name__=='__main__':
    main()
