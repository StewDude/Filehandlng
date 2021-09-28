#import threading

import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    return f"Done sleeping for...{seconds} seconds"

with concurrent.futures.ThreadPoolExecutor() as exec:
    seconds = [5, 4, 3, 2, 1]
    results = exec.map(do_something, seconds)

    for resut in results:
        print(resut)
#    for f in concurrent.futures.as_completed(results):
#        print(f.result())
#    f1 = exec.submit(do_something, 1.5)
#    f2 = exec.submit(do_something, 1.0)

#    print(f1.result())
#    print(f2.result())

threads = []

#for _ in range(10):
#    t = threading.Thread(target=do_something, args = [1.5])
#    t.start()
#    threads.append(t)

#for thread in threads:
#    thread.join()


finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s)")