def func():
    print "hey there demo " + __name__ #print statement prints the name of the program (__main__)

#but if we call this demo module from another module, the same print statement will not print "__main__" but they
# will print the name of the module as now the main program is the current module which we are calling it from, and not the demo module.
#In OTHER WORDS, __name__ is a VARIABLE which holds the value "__main__" when the same program is executed and
# holds the value "__<filename>__" (demo in this case) when called from a different module.



if __name__ == "__main__": # if i want to call the function only when i execute the demo.py itself,
    func()              # then i create an if condition
else:
    print "demo executed from some other module"
