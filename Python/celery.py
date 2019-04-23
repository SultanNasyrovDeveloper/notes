
# ИНФОРМАЦИЯ:
# ===========
# Celery - распределенная очередь заданий. Есть некая очередь в которую поступают
# задачи, а после распределяются между worker(исполнителями).
# Брокер(Celery) отвечает за передачу сообщений(задач) между исполнителями.
# Бекэнд - хранилище результатов выполнения задач.

# ВОЗМОЖНОСТИ:
# ============
# - Выполнять задачи асинхронно и синхронно
# - Выполнять переодические задачи
# - Выполнять отложенные задачи
# - Распределенное выполнение(Запущен на нескольких серверах)
# - Конкурентное выполнение задач

# СОВЕТЫ ПО РАБОТЕ:
# =================
# - идемпотентные задачи(при повторном запуске задачи с этим же объектом не должно быть другого результата)
# - минимум логики в задаче
# - заранее продуманный retry policy для каждой задачи(max_retries, retry_backoff)
# - приоритируй задачи(priority)
# - worker_max_memory_per_child - обязательно проставить лимит памяти на worker
# - не используй базу данных в качестве бекэнда
# - разделяй задачи по очередям
# - логируй ошибки
# - старайся указывать лимит времени на выполнение задачи (soft_time_limit, time_limit, expires)
# - не храни результаты без необходимости(ignore_result=True)
# - используй Flower для мониторинга
# - не передавай ORM объект в качестве аргумента к задаче, лучше идентификатор
# - не используй Celery для выполнения долгих задач(Какая задача считается долгой???)

# МОНИТОРИНГ:
# ===========
# - Справляется ли текущая конфигурация с нагрузкой?
# - Какая есть деградация времени выполнения задач?

# CONFIGURATION:
# ==============
# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379'/
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']  # allowed types
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE='UTC'  # timezone used inside celery


# CELERY APPLICATION INSTANCE(DJANGO):
# ====================================
# Celery library must be instanciated before use
# this instance called app(thread-safe)
# my_project/my_project/celery.py
import os
from celery import Celery

# set django setting as celery settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

# instanciate new celery app
app = Celery('project_name')

# configurate it
# load Celery settings(starts with CELERY_ prefix)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Find all task inside the project
app.autodiscover_tasks()

# insure that celery app loaded with django
# my_project/my_project/__init__.py
from .celery import app as celery_app

__all__ = ('celery_app',)


# CREATE TASKS:
# =============
# task can be created of any callable

# tasks.py
from celery.task import task

# task options
    bind=bool()  #
    queue='Queue name'
    typing=bool()  # disable task argument checking
    time_limit=int(seconds)  # hard time limit
    soft_time_limit=int(seconds)  # soft time limit(whats the difference)
    ignore_result=bool()  # if False will not store task result in db
    store_errors_even_if_ignored=bool()

# basic task creation
# --------------------
@app.task  # base task decorator
# or
@shared_task  # django task decorator(can be set without app instance)
def celery_task(x, y):
    return x + y

# task inheritance
# -----------------
from celery import Task

class CustomTask(Task):
    pass

@task(base=CustomTask)
def celery_task(x, y):
    return x + y

# task request
# -------------
# contains info and state of currently executing task
    id  # task idea
    args  # positional arguments
    kwargs  # keyword arguments
    expires  # progonal expiry time
    timelimit  # tuple of current limit (soft, hard)
    link  # add callback function(only if success)
    # retry policy
    max_retries  # max number of retries before giving up
    retries  # how many times this task was retied
    interval_start  # number of seconds between max_retries
    interval_step  # this number will be added to delay every retry
    interval_max   # max seconds to wait

@app.task(bind=True)
def dump_context(self, x, y):
    print('Executing task id {0.id}, kwargs: {0.kwargs!r}'.format(self.request))


# CALL TASKS:
# ===========
# standart set of functions to call a task
# -----------------------------------------

# delay method doesn't support
task.delay(arg, arg2, kwarg=kwarg_value)  # send task mesage with given args and kwargs
task.apply_async((arg, arg2), {kwarg: kwarg_value}) # send task mesage with given args and kwargs
    args  # tuple of positional arguments
    kwargs  # dict of keyword args
    countdown  # number of seconds to wait until task execution
    eta  # (estimated time of arrival) absolute datetime when task should be executed
    expires  # datetime or seconds in the future the task wont be executed after

# task progress
# --------------
@app.task(bind=True)
def hello(self, a, b):
    self.update_state(state="PROGRESS", meta={'progress': 50})
    self.update_state(state="PROGRESS", meta={'progress': 90})
    return 'hello world: %i' % (a+b)


# DESIGNING WORK FLOWS:
# =====================

# task signature
# ---------------
# sometimes you want to pass the signature of a task invocation to another process
# or as an argument to another function
from celery import signature

# you can create signature using task name
signature('tasks.task_name', args=(args1, args2), countdown=3)
# you can use tasks signature method
task.signature((arg, arg2), countdown=3)
# you can use shortcuts for this
task.s()

# partial signature

# callbacks
# ---------
# callbacks can be added to any task using link argument to apply_async()
task.apply_async((arg, ), link=callback_task.s(arg))

# chains
# -----------
# chain is linked tasks
from celery import chain

# tasks execute and pass their return value to the next task
result = chain(task1.s(2, 2), task2.s(4), task3.s(8))()


# WORKER
# =======
# start worker
# ------------
# some file path arguments can contain variables
# ocs.celeryproject.org/en/latest/userguide/workers.html#variables-in-file-paths
celery -A app_name worker
    -B  # also run celery periodict task scheduler
    -Q queue1,queue2  # list of queues to enable
    -X queue1, queue2  # list of queues to disable
    -I foo.tasks,bar.tasks  # list of additional modules to import
    --time_limit  #
    --soft_time_limit  #
    # logging
    -f path  # path to file
    -l info  # loglevel

# broadcast function
# this client method used to send commands to the function


# PERIODIC TASK
# ==============

# celery beat
# ------------
# is a scheduler. it launches task at regulat intervals

# entries
# --------
# to call the task periodically you have to add an entry to the beat scheduler

# variant 1
from celery import Celery
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'))
@app.task
def test(arg):
    print(arg)

# variant 2
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0/crontab(hour=7, minute=35, day_of_week=3),
        'args': (16, 16)
    },
}
# possible fields
    task  # task name
    schedule  # task schedule
    args  # positional args
    kwargs  # keyword args
    options  # dict of any apply_async supported keyword args

# cronrab schedules
# -----------------
# use if you want more complex schedules

# task will be repeated every Wednesday at 7.35
crontab(hour=7, minute=35, day_of_week=3)

# more Examples
# crontab(hour=7, minute=35, day_of_week=3)
# project.org/en/latest/userguide/periodic-tasks.html#crontab-schedules


# ROUTING
# ========
# automatic routing
# ------------------
# the simplest way to do routing is to use the task_create_missing_queues setting
# With this setting on, a named queue that’s not
# already defined in task_queues will be created automatically.

# you can change name of default queue

# manual routing
# ---------------



# LOGGING:
# ========
# logging
# контролировать вывод ошибок можно через стандартный python logging,
# достаточно повесить свой handler на logger под названием "celery".
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# starting worker process
celery -A my_project worker -l info
celery help
celery worker --help
