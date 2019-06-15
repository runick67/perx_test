import aiohttp_jinja2

from forms import TaskForm
from task import Task
from tasks_queue import TasksQueue


task_queue = TasksQueue()


@aiohttp_jinja2.template('index.html')
async def index(request):
    """ Represents main web page

    :param request: HTTP request
    :return: HTTP response
    """
    return response(TaskForm())


@aiohttp_jinja2.template('index.html')
async def post_task(request):
    """ Uses for creating a task

    :param request: HTTP POST request
    :return: HTTP request
    """
    data = await request.post()
    form = TaskForm(data)
    if form.validate():
        task = Task(form.count.data, form.delta.data,
                    form.start.data, form.interval.data)
        task_queue.add_task(task)
        form = TaskForm()
        form.task_added = True
    return response(form)


def response(form):
    """ Returns common template dictionary

    :param form: TaskForm
    :return: common template dictionary
    """
    return {'running_tasks': task_queue.running_tasks,
            'tasks': task_queue.tasks, 'form': form}
