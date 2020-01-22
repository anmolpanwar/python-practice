def checkstr(sample):
    newstr = ""
    for i in sample:
        if i=='0' or i == '1' or i == '2' or i == '3' or i == '4'or i == '5'or i == '6'or i == '7'or i == '8'or i == '9':
            newstr+=i

    if sample[0]=="-":
        print "-"+newstr


    else:
        print newstr


inputstring = raw_input()
checkstr(inputstring)




str = input()
str_list=list(str)
res = ''.join(filter(lambda i:i.isdigit(),str))

if str_list[0]=='-':
    print ("-"+res)
else:
    print(res)
