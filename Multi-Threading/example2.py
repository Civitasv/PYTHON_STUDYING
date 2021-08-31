import time
import concurrent.futures

start = time.perf_counter()


def do_somthing(second):
    print("Sleeping {} second...".format(second))
    time.sleep(second)
    return "Done Sleeping {}".format(second)


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_somthing, 1) for _ in range(2)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(do_somthing, [6, 2, 3, 4, 5])

    for result in results:
        print(result)


finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))
