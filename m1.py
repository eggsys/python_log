class main_file(object) :
    def __init__(self) -> None:
        pass
        print("init")
        self.title = ("Rungkrit")
        self.first(self.title)


    def first(self, name):
        print("say hello to :",name)

    def method(self, arg1, arg2):
        print ("in method (args):", arg1, arg2)
    
    def wtf():
        print("wut di faq why u call me ?")


class secondary(object):
    def __init__(self, *arg):
        #pass
        self.arg = arg
        self.main_file = main_file()
        self.dosomething()

        
    def dosomething(self):
        print("do something la")
        print(m.title)
        x =  main_file.wtf()
    def myfunc(a,b, *args, **kwargs):
      c = kwargs.get('c', None)
      d = kwargs.get('d', None)

      print("c :", c)
      print("d :", d)


#m = main_file()
#s = secondary(m)
#main_file.method(s, "egg" ,2)

#s.myfunc("x","y",  d='dog', c='nick',)
