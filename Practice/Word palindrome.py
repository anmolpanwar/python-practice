def is_palindrome(word):
    newword = word.lower()

    list1 = list(newword.strip())

    strn = ''
    list1.reverse()

    for i in list1:
        strn+=i

    pal = newword+strn

    if strn == newword:
        print True
    else:
        print "Palindrome of this will be: " + pal


is_palindrome('dfsbj')


