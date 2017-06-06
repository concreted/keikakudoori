import time
import json
import celery
from celery import Celery
from redbeat.schedulers import RedBeatSchedulerEntry

from tasks import add


# ======== Test basic task ========
# result = add.delay(2,3)
# time.sleep(1)
# print result.get()

# ======== Test adding cron by Python ========

# Need to initialize an app with same config as running Celery app
app = Celery('tasks')
app.config_from_object('celeryconfig')

cron = celery.schedules.crontab(minute="1", hour="1")
entry = RedBeatSchedulerEntry('test7', 'tasks.add', cron, args=[5, 1], app=app)
entry.save()


# ======== Test adding cron by Redis ========
# import redis
# r = redis.StrictRedis(host='localhost', port=6379, db=1)

# cron_def = {
#     "name": "test_direct_insert_2",
#     "task": "tasks.add",
#     "schedule": {
#         "__type__": "crontab",
#         "minute": "5",  # optional, defaults to *
#         "hour": "1",  # optional, defaults to *
#         "day_of_week": "*",  # optional, defaults to *
#         "day_of_month": "*",  # optional, defaults to *
#         "month_of_year": "*",  # optional, defaults to *
#     },
#     "args": [  # optional
#         15,
#         16
#     ],
#     # "kwargs": {  # optional
#     #     "max_targets": 100
#     # },
#     "enabled": True,  # optional
# }

# # Note: The key name after redbeat: must match the name in the definition. If not,
# # Redbeat will automatically insert a new key matching the def name to hold metadata
# # for the task.
# r.hmset('redbeat:%s' % cron_def['name'], {"definition": json.dumps(cron_def)})
# print r.hgetall('redbeat:test_direct_insert')

# # current_utc_epoch_time = time.mktime(datetime.datetime.now().timetuple())

# r.zadd('redbeat::schedule', 0, 'redbeat:%s' % cron_def['name'])



# # ========= Testing time ==========
# import calendar
# import datetime
# app = Celery('tasks')
# app.config_from_object('celeryconfig')

# print 'PYTHON TIME'
# print datetime.datetime.now()
# print time.mktime(datetime.datetime.now().timetuple())

# print 'APP TIME'
# print app.now()
# print time.mktime(app.now().timetuple())

# print 'STRFTIME'
# print datetime.datetime.utcnow()
# print int(datetime.datetime.utcnow().strftime('%s'))
