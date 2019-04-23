"""
asyncio 3.5.6

library to write concurrent code
"""

Event Loops
-------------
управляет выполнением задач: регистрирует и запускает в подходищий момент

asyncio.get_event_loop() - get event loop for current context
asyncio.set_event_loop(loop)  - set event loop for current context
asyncio.new_event_loop()  - create and return a new event loop
use set_event_loop() to set the loop for current context

Run event loop
--------------
.run_forever()  - run until stop() method is called
.run_until_complete() - run until Future is done
.is_running() - running status of event loop
.stop() - stop running loop


Tasks(Futures) and Coroutines
------------------------------
Корутины - запускаются церез цикл. Обязательно содержат await.
При помощи await мы отдаем управление фукнцией циклу event_loop
корутины могут быть запущены из другой корутины или обернуты в задачу с помощью
create_task()

wait() - объединяет задачи


import asyncio

async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context switch to foo again')

async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()


Future
------
Хранит результат выполнения какой либо задачи.
Он держатель для результата или исключения,
а также списка обратных вызовов после выполнения.
