import time
import concurrent.futures
import asyncio
start = time.perf_counter()


def do_somthing(second):
    print("Sleeping {} second...".format(second))
    time.sleep(second)
    return "Done Sleeping {}".format(second)


async def do_async():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(do_somthing, 1) for _ in range(2)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())


async def main():
    task = asyncio.create_task(do_async())
    await task
    print("ss")

asyncio.run(main())

finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))
