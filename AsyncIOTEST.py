import asyncio

async def TEST1(parameter_list):
    a = 0
    while a < 5:
        a += 1
        print(parameter_list)
        await asyncio.sleep(0.1)

async def Test2():
    t0 = "ага, да"
    a = 0
    while a < 5:
        a += 1
        print(t0)
        await asyncio.sleep(0.5)

async def main():
    task1 = asyncio.create_task(TEST1("da"))
    task2 = asyncio.create_task(Test2())
    await asyncio.gather(task1,task2)
    print("END")

asyncio.run(main())
