import time
import sys
sys.setrecursionlimit(5000)

def stateful_function(func):
    cache = {}
    def inner(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner 


@stateful_function
def fibonacci(n):
    "Ola"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
  
start = time.time()    
print(fibonacci(20))
end = time.time()
print(end - start)
