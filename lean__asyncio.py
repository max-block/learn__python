import asyncio


async def task1():
    print("task1")
    await asyncio.sleep(1)


async def task2():
    print("task2")
    await asyncio.sleep(1)


def main():
    loop = asyncio.new_event_loop()
    loop.create_task(task1())
    loop.create_task(task2())
    loop.run_forever()


if __name__ == "__main__":
    main()
