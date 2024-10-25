'''
Asynchronous programming allows you to write concurrent code that runs in a single thread.
Every time a new thread is created, some memory is used to allow context switching. If we use async programming, 
this is not a problem since the code runs in a single thread.


To write asynchronous code in python, import the library using import asyncio.

Asyncio has 3 main components:

    1. Coroutine
    A coroutine is the result of an asynchronous function which can be declared using the keyword async before def.

    async def my_function(argument):
        pass

    When we declare a function using the async keyword the function is not executed; instead, a coroutine object is returned.

    To call a coroutine, write

    my_coroutine = my_function(argument)

    There are two ways to read the output of an async function from a coroutine. The first way is to use the await keyword, 
    which is only possible inside async functions and will wait for the coroutine to terminate and return the result.

    result = await my_function(argument)

    The second way is to add it to an event loop.

    2. Event Loop

    The event loop is the object which executes our asynchronous code and decides how to switch between async functions. 
    After creating an event loop we can add multiple coroutines to it; these coroutines will all be running concurrently 
    when run_until_complete or run_forever is called.

    loop = asyncio.new_event_loop()  # create loop
    future = loop.create_task(my_coroutine) # add coroutine to the loop
    loop.run_until_complete(future) # add coroutine to the loop concurrently
    loop.close() # close the loop


    3. Future

    A future is an object that works as a placeholder for the output of an asynchronous function, and it gives 
    us information about the function state. A future is created when we add a coroutine to an event loop. 

    future = loop.create_task(my_coroutine)

    The method adds a coroutine to the loop and returns a task which is a subtype of the future.


In asynchronous programming, the execution of a function is usually non-blocking. In other words, 
each time you call a function it returns immediately. However, that function does not necessarily 
get executed right away. Instead, there is usually a mechanism (called the “scheduler”) which is 
responsible for the future execution of the function.

The problem with asynchronous programming is that a program may end before any asynchronous function starts. 
A common solution for this is for asynchronous functions to return “futures” or “promises”. 
These are objects that represent the state of execution of an async function. Finally, asynchronous programming 
frameworks typically have mechanisms to block or wait for those async functions to end based on those “future” objects.

'''