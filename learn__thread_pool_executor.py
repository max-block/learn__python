import random
import time
from concurrent.futures._base import as_completed
from concurrent.futures.thread import ThreadPoolExecutor


def t1():
    def job(a):
        time.sleep(random.random())
        return a * 2

    with ThreadPoolExecutor(max_workers=50) as executor:
        future_to_param = {}
        for i in range(30):
            future_to_param[executor.submit(job, i)] = i

        for future in as_completed(future_to_param):
            result = future.result()
            print(f"{future_to_param[future]} -> {result}")


if __name__ == "__main__":
    t1()
