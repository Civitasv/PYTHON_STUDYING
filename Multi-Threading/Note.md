# 多线程

python 中的多线程使用`threading`模块，在 IO 密集型任务（如文件上传、文件下载）中有很大作用，对于计算密集型任务，应使用`multi-processing`模块使用函数式编程进行并行化处理。

一个简单的例子：

```py
import time

start = time.perf_counter()


def do_something():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping")

do_something()
do_something()

finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 2)))

```

这时会打印如下结果：

```txt
Sleeping 1 second...
Done Sleeping
Sleeping 1 second...
Done Sleeping
Finished in 2.0 second(s)
```

此时为顺序执行，先执行一个耗时事件`do_something`，再执行另一个耗时事件`do_something`，最后`Finished`

计算机在 IO 密集型任务时，CPU 并未被使用，因此，可以使该工作挂起，继续处理其他任务，这时线程就有其作用了，修改该实例，添加线程处理：

```py
import time
import threading

start = time.perf_counter()


def do_somthing():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping")


t1 = threading.Thread(target=do_somthing)
t2 = threading.Thread(target=do_somthing)

t1.start()
t2.start()

finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))
```

此时会打印如下结果：

```txt
Sleeping 1 second...
Sleeping 1 second...
Finished in 0.0 second(s)
Done Sleeping
Done Sleeping
```

这是因为任务 t1 和 t2 均被线程挂起。

实际工作中，我们还可能想要耗时事件 1 和事件 2 同时执行，执行完毕之后再执行下面的代码，此时，需要引入`join`函数：

```py
import time
import threading

start = time.perf_counter()


def do_somthing():
    print("Sleeping 1 second...")
    time.sleep(1)
    print("Done Sleeping")


t1 = threading.Thread(target=do_somthing)
t2 = threading.Thread(target=do_somthing)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))
```

此时，将打印：

```txt
Sleeping 1 second...
Sleeping 1 second...
Done Sleeping
Done Sleeping
Finished in 1.0 second(s)
```

很好，代码已经按预期工作了。

**如何向代码中传参呢？**

Thread 构造器的 args 参数允许我们向目标函数传递参数，如下：

```py
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
```

打印结果为：

```txt
Sleeping 1.5 second...
Sleeping 1.5 second...
Done Sleeping
Done Sleeping
Finished in 1.5 second(s)
```

python 还提供了线程池模块，能够简化使用。

使用`concurrent.futures`模块改写上面的例子：

```py
import time
import concurrent.futures

start = time.perf_counter()


def do_somthing(second):
    print("Sleeping {} second...".format(second))
    time.sleep(second)
    return "Done Sleeping"


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_somthing, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print("Finished in {} second(s)".format(round(finish-start, 1)))

```

此时将打印：

```txt
Sleeping 1 second...
Sleeping 1 second...
Done Sleeping
Done Sleeping
Finished in 1.0 second(s)
```

我们还可以使用`executor.map`函数：

```py
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(do_somthing, [1, 2, 3, 4, 5])

    for result in results:
        print(result)
```

注意，即使我们不获取 results，`submit`和`map`函数也会等待函数执行完毕后再执行下面的其他代码。

## 实例：图片下载

下面我们使用图片下载作为示例。

```py
import requests
import time
import concurrent.futures

img_urls = ["https://unsplash.com/photos/W3TInIIf7LM/download?force=true",
            "https://unsplash.com/photos/mn2tsPe6Oe8/download?force=true",
            "https://unsplash.com/photos/UzoOegEd3Q0/download?force=true",
            "https://unsplash.com/photos/xRcxjgvJrrU/download?force=true",
            "https://unsplash.com/photos/TLmG9n12kng/download?force=true"]
start = time.perf_counter()


def download_file(img_url):
    r = requests.get(img_url)
    content = r.content
    img_name = img_url.split("/")[4]
    img_name = "Multi-Threading\images\{}.jpg".format(img_name)
    with open(img_name, "wb") as img_file:
        img_file.write(content)
        print("{} was downloaded".format(img_name))


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_file, img_urls)

end = time.perf_counter()

print("Finished in {} second(s)".format(round(end-start, 1)))
```
