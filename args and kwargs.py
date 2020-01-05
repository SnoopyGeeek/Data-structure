from functools import wraps
from collections import OrderedDict
from inspect import signature
from functools import lru_cache
def test1(*args,**kwargs):
    return (*args,None,*kwargs)
def test2(*args,**kwargs):
    return (*args,None,*kwargs)

def lru_cache_by_me(max_size=120):
    def lru_wrapper(func):                           # lru_cache implementation with ordereddic and signature
        func_sig=signature(func)
        cache=OrderedDict()
        '''lru_wrapper doc'''
        @wraps(func)
        def wrapped(*args,**kwargs):
            '''wrapped doc'''
            bind=func_sig.bind(*args,**kwargs)
            bind.apply_defaults()
            key=(bind.args,tuple(sorted(bind.kwargs.items())))
            #print(key)
            try:
                val=cache[key]
                del cache[key]
            except KeyError:
                val=func(*args,**kwargs)
            cache[key]=val
            if max_size and len(cache)>max_size:
                cache.popitem(last=False)
            return val
        return wrapped
    return lru_wrapper

def fun_example():
    '''fun doc'''
    print("fucker")

def test(fn):
    signature=signature(fn)
    def call(*args,**kwargs):
        bind=signature.bind(*args,**kwargs)
        bind.apply_defaults()
        return bind.args,tuple(sorted(bind.kwargs.items()))
    return call

def fn1(a,b,c=1,d=2,**kwargs):
    pass
def fn2(a,b,*args,c=1,d=2,**kwargs):
    pass

@lru_cache(None)
def Catlan(n):
    if n==0:
        return 1
    result=0
    for i in range(0,n,2):
        result+=Catlan(i)*Catlan(n-2-i)
    return result
    
if __name__=="__main__":
    #print(test2(5,6,a=2,b=3))
    #fun_example()
    #print(fun_example.__name__)
    #print(fun_example.__doc__)
    print(Catlan(50))
    print(Catlan.cache_info())
    