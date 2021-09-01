import time
import threading

start = time.perf_counter()


def do_somthing(second):
    time.sleep(second)
    print("Done Sleeping")


def do_print():
    for _ in range(100):
        print(1)


threads = []

t = threading.Thread(target=do_somthing, args=[0.001])
t2 = threading.Thread(target=do_print)
t.start()
t2.start()
threads.append(t)
threads.append(t2)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))
