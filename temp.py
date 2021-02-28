import asyncio
from asyncio.windows_events import INFINITE

var = 0

async def periodic():
    global var, loop
    while True:
        print('periodic')
        await asyncio.sleep(.5)
        var += 1

        if var == 1000:
            loop.stop()
            break
    print("Exited loop")

def stop(): 
    task.cancel()

loop = asyncio.get_event_loop()
loop.call_later(INFINITE, stop)
task = loop.create_task(periodic())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
