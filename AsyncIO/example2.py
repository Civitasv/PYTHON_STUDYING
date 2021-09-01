import asyncio


async def main():
    print("Tim")
    task = asyncio.create_task(foo("text"))
    # if remove the line below, it will print Tim, finished and then text
    await task
    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
