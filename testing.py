import multiprocessing
import time

def func():
    for i in range(0, 10):
        print("Hello world", i)
        time.sleep(0.001)

if __name__ == '__main__':
    thread1 = multiprocessing.Process(target=func)
    thread2 = multiprocessing.Process(target=func)

    thread1.start()
    thread2.start()
