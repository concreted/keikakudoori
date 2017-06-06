from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
# app = Celery('tasks', backend='redis://localhost', broker='pyamqp://guest@localhost//')
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y

# app.conf.beat_schedule = {
#     'add-every-10-seconds': {
#         'task': 'tasks.add',
#         'schedule': 10.0,
#         'args': (16, 16)
#     },
# }
