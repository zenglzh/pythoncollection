class entryExit(object):
    
    def __init__(self, f):
        print("inside my Decorator.__init__()")
#         f()  # Prove that function definition has completed
        self.f = f
        
    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entryExit
def func1():
    print("inside func1()")


@entryExit
def func2():
    print("inside func2()")

func1()
func2()
