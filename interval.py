from threading import Timer
import asyncio

class Interval(object):

    # Repeats a function every specified interval
    # 
    # @param self: class itself
    # @param interval: inteveral between repition
    # @param function: function to repeat
    # 
    def __init__(self, interval, function):
        # Runs the function at a specified interval with given arguments.
        self.interval = interval
        self.function = function
        self.running  = False 
        self._timer   = None 

    def __call__(self):
        # Handler function for calling the function and continuting. 

        self.running = False  # mark not running
        self.start()          # reset the timer for the next go 
        asyncio.run(self.function())       # call the partial function 

    def start(self):
        # """
        # Starts the interval and lets it run. 
        # """
        if self.running:
            # Don't start if we're running! 
            return 
            
        # Create the timer object, start and set state. 
        self._timer = Timer(self.interval, self)
        self._timer.start() 
        self.running = True

    def stop(self):
        # """
        # Cancel the interval (no more function calls).
        # """
        
        if self._timer:
            self._timer.cancel() 
        self.running = False 
        self._timer  = None
    
    # def asyncio_run(future, as_task=True):

    #     # A better implementation of `asyncio.run`.
    #     # :param future: A future or task or call of an async method.
    #     # :param as_task: Forces the future to be scheduled as task (needed for e.g. aiohttp).
    #     try:
    #         loop = asyncio.get_running_loop()
    #     except RuntimeError:  # no event loop running:
    #         loop = asyncio.new_event_loop()
    #         return loop.run_until_complete(_to_task(future,as_task,loop))
    #     else:
    #         nest_asyncio.apply(loop)
    #         return asyncio.run(_to_task(future, as_task, loop))
    
    # def _to_task(future, as_task, loop):
    #     if not as_task or isinstance(future, Task):
    #         return future
    #     return loop.create_task(future)