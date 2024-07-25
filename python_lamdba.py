#!./bin/python3

def helloworld(x:int) -> object:
    print(x)
    return "hello world"
    pass

print(helloworld("hello"))

fun = lambda x:x+1
print(fun(1))
print(list(map(lambda x:x+1,[1,2,3])))




