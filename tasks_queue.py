import asyncio
from datetime import datetime


class TasksQueue:
    """ The class represents queue
    """

    MAX_TASK_QUEUE = 1

    def __init__(self):
        """ Initializer

        """
        self.tasks = []
        self.running_tasks = []

    def add_task(self, task):
        """ Adds task to queue

        :param task: Task to add
        """
        self.tasks.append(task)
        self.check_if_can_run()

    def check_if_can_run(self):
        """ Check if can run task

        """
        if len(self.running_tasks) < self.MAX_TASK_QUEUE and self.tasks:
            task = self.tasks.pop(0)
            self.running_tasks.append(task)
            task.date_of_start = datetime.now()
            asyncio.ensure_future(self.run_task(task))

    async def run_task(self, task):
        """ Runs task

        :param task: task to run
        """
        await task.run()
        self.running_tasks.remove(task)
        self.check_if_can_run()
