import time
import sys
sys.setrecursionlimit(5000)

def fibonacci(n):
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
