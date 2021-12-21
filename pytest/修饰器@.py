#@修饰器
import time

#原始实现功能
# def foo():
    # start = time.perf_counter()  #开始计时
    # print("in foo()")            #耗用时间
    # end = time.perf_counter()   #结束计时
    # print("Time Elapsed:",end - start)

# foo()


#改进实现功能，将计时函数独立出来一个函数，然后将需要计时的函数当
#参数传递给计时函数，然后计时函数再调用
# def foo():
    # print("in foo()")

# def timeit(func):  #传递函数
    # start = time.perf_counter()
    # func()   #函数调用
    # end = time.perf_counter()
    # print("Time Elapsed:",end - start)

# timeit(foo)



#使用函数嵌套的方式

def foo():
    print("in foo()")

## 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
def timeit(func):
    def wrapper():  
        start = time.perf_counter()
        func()  
        end = time.perf_counter()
        print("Time Elapsed:",end - start)
     
    # 将包装后的函数返回
    return wrapper

# foo = timeit(foo) #对foo函数装修饰
# foo()   #对修饰后的foo函数调用


#sandwich 例子
def bread(func):
    def wrapper():
        print("<'''      '''/>")
        func()
        print("<____________/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes")
        func()
        print("salad")
    return wrapper

# sandwich = bread(ingredients(sandwich))

# sandwich()

@bread   #@是上面这种写的python语法糖写法
@ingredients  #@是上面这种写的python语法糖写法
def sandwich(food="--ham--"):
    print(food)

## 一个参数写法,闭包函数必须保持参数个数一致
def w1(fun):
    def wrapper(name):
        print("this is the wrapper head")
        fun(name)
        print("this is the wrapper end")
    return wrapper

@w1
def hello(name):
    print("hello "+name)
    
# hello("张三")

#多个参数的
def w2(func):
    def wrapper(*args,**kwargs):
        print("this is the wrapper head")
        func(*args,**kwargs)
        print("this is the wrapper end")
    return wrapper

@w2
def hello2(name,age):
    print("hello"+name+" , "+age)
hello2("张三","32")




