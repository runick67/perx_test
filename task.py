import asyncio
from datetime import datetime


class Task:
    """ The class represents Task
    """

    def __init__(self, count, delta, start, interval):
        """ Initializer

        :param count: count of elements
        :param delta: delta between elements
        :param start: start element
        :param interval: interval in seconds between iterations
        """
        self.count = count
        self.delta = delta
        self.start = start
        self.interval = interval
        self.current = self.start
        self.date_of_start = None

    async def run(self):
        """ Runs the task

        """
        if not self.date_of_start:
            self.date_of_start = datetime.now()
        for i in range(1, self.count):
            self.current += self.delta
            await asyncio.sleep(self.interval)
