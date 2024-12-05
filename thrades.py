import time
import threading

def func(kk):
    print(f"it execute in{kk}")
    # time.sleep(kk)
# func(4)
# func(6)
# func(7)
t1=threading.Thread(target=func,args=[5])
t2=threading.Thread(target=func,args=[3])
t3=threading.Thread(target=func,args=[7])

t1.start()
t2.start()
t3.start()