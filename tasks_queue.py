import asyncio
import functools
from datetime import datetime


class TasksQueue:
    """ The class represents queue
    """

    MAX_TASK_QUEUE = 1

    def __init__(self):
        """ Initializer

        """
        self.tasks = []
        self.semaphore = asyncio.Semaphore(self.MAX_TASK_QUEUE)

    @property
    def running_tasks(self):
        """ Returns list of running tasks

        :return: list of running tasks
        """
        return list(filter(lambda task: task.date_of_start, self.tasks))

    @property
    def task_in_queue(self):
        """ Returns list of not running tasks

        :return: list of not running tasks
        """
        return list(filter(lambda task: not task.date_of_start, self.tasks))

    def on_task_done(self, task, _):
        """ Callback that calls when task done

        :param task: Task
        """
        self.tasks.remove(task)

    def add_task(self, task):
        """ Adds task to queue

        :param task: Task to add
        """
        self.tasks.append(task)
        fut = asyncio.ensure_future(self.run_task(task))
        if not self.semaphore.locked():
            task.date_of_start = datetime.now()
        fut.add_done_callback(functools.partial(self.on_task_done, task))

    async def run_task(self, task):
        """ Runs task

        :param task: task to run
        """
        async with self.semaphore:
            await task.run()
