def dec(fun):
    def inner(*args,*kwagrs):
        fun()
        print ("function decorated")
    return inner

@dec
def func():
    print ("function normal")

func()
