import time
import concurrent.futures
start = time.perf_counter()


def do_somthing(second):
    print("Sleeping {} second...".format(second))
    time.sleep(second)
    return "Done Sleeping {}".format(second)


def do_async():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(do_somthing, 1) for _ in range(2)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(do_async)

    print("ss")


main()
finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))
