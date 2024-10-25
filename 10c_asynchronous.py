# Multiple Task

import asyncio

async def square(x):
    print('Square', x)
    await asyncio.sleep(1)
    print('End square', x)
    return x * x

# Create event loop
loop = asyncio.get_event_loop()

# Run async function and wait for completion
results = loop.run_until_complete(asyncio.gather(
    square(1),
    square(2),
    square(3)
))
print(results)

# Close the loop
loop.close()

'''
Basically, we use asyncio.gather(*tasks) to inform the loop to wait for all tasks to finish. 
Since the coroutines will start at almost the same time, the program will run for only 1 second. 
Asyncio gather() won’t necessarily run the coroutines by order, although it will return an ordered list of results.
'''