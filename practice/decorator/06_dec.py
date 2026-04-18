# Timing Decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Staring time:", start)
        print('Ending time:',end)
        print("Time taken:",end - start)
    return wrapper

@timer
def loop_test():
    for i in range(1000000):
        pass

loop_test()