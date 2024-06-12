class DecoratorClass:
    def __init__(self,func)-> None:
        self.func = func
        pass
    def __call__(self,*args,**kwargs):
        print("before")
        self.func(*args,**kwargs)
        print("after")
        pass

    def sayHello(self) -> str:
        return "hello world"




@DecoratorClass
def my_function():
    print("my function")
    pass



my_function()
