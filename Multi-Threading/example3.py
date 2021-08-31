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
