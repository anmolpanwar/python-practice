#caesar cipher
def caesar(tex,key):
    text = tex.lower()
    ascii = []
    ls = list(map(str, text.strip()))
    for i in range(len(ls)):
        if ord(ls[i])>96 and ord(ls[i])<123:
            shift = ord(ls[i]) + (key%26)
            if shift>122:
                shift = 96 + shift-122
            else:
                pass
            ascii.append(shift)
        else:
            ascii.append(ord(ls[i]))

    ls1 = [chr(i) for i in ascii]
    return ''.join(ls1)
if __name__ == '__main__':
    text = input("Enter the text: ")
    print (caesar(text,int(input("Enter the key: "))))
