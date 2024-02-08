# ************************  AsyncIO in Python  ************************

# AsyncIO is a library to write concurrent code using the async/await syntax. It is a single-threaded, single-process design, which means it will not make use of multiple cores. It is perfect for IO-bound operations.

# Example:

import asyncio

async def count():
    print("One")
    await asyncio.sleep(2)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

    # await count()   # these will run sequentially 
    # await count()
    # await count()

asyncio.run(main())
