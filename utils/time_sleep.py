import asyncio


async def time_(minutes: int):
    count = 0
    while minutes != count:
        print(count + 1)
        await asyncio.sleep(1)
        count += 1
