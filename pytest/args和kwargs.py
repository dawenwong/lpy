# 可以看到，这两个是python中的可变参数。
# *args表示任何多个无名参数，它是一个tuple；
# **kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，
# 必须*args参数列要在**kwargs前，
# 像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，
# 会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。

def foo(*args,**kwargs):
    print('agrs = ', args)
    print('kwargs = ',kwargs)
    print('______________________________')
    
if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3,d=4)
    foo(1,2,3,a=1,b=2,c=3)
    #foo(a=1,b="2",1,2,c=3,3)#SyntaxError: positional argument follows keyword argument
    
    foo('a',1,1>3,a=1,b='hello',c=3)
    
