'''
Sometimes results may be needed as soon as they are available. For that, we can use a second 
coroutine that deals with each result using asyncio.as_completed()
'''

import asyncio

async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x * x

# Create event loop
loop = asyncio.get_event_loop()

async def when_done(tasks):
    for res in asyncio.as_completed(tasks):
        print('Result:', await res)

loop.run_until_complete(when_done([
    square(1),
    square(2),
    square(3)
]))