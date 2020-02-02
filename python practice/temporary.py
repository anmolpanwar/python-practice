from time import time
def dec(fun):
    def inner():
        fun()
        print (time())
    return inner

@dec
def func():
    print ("function normal")

func()
