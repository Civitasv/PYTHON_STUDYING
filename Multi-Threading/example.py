import time
import threading

start = time.perf_counter()


def do_somthing(second):
    print("Sleeping {} second...".format(second))
    time.sleep(second)
    print("Done Sleeping")


threads = []

for _ in range(2):
    t = threading.Thread(target=do_somthing, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))
