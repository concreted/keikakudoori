from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime, timedelta

from tasks import add

def publish_sequence(device_id=None, group_id=None, sequence=None):
    if sequence is None:
        sequence = {}

    if not (device_id or group_id):
        print 'Expected device_id or group_id'
        return
    q = Queue('default', connection=Redis())
    result = q.enqueue(add, 1, 2)

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue

# publish_sequence(device_id='moo', sequence={'hello': 'world'})
print datetime.utcnow()
print datetime.utcnow() + timedelta(seconds=20)
# Run in 10 seconds
# scheduler.enqueue_at(datetime.utcnow() + timedelta(seconds=10), add, 1, 2)

# Run every X seconds X times
# scheduler.schedule(
#     scheduled_time=datetime.utcnow(), # Time for first execution, in UTC timezone
#     func=add,                     # Function to be queued
#     args=[1, 2],             # Arguments passed into function when executed
#     # kwargs={'foo': 'bar'},         # Keyword arguments passed into function when executed
#     interval=15,                   # Time before the function is called again, in seconds
#     repeat=10                      # Repeat this number of times (None means repeat forever)
# )

# Cron: run every minute
scheduler.cron(
    '* * * * *',                # A cron string (e.g. "0 0 * * 0")
    func=add,                  # Function to be queued
    args=[1, 2],          # Arguments passed into function when executed
    # kwargs={'foo': 'bar'},      # Keyword arguments passed into function when executed
    repeat=None                   # Repeat this number of times (None means repeat forever)
    # queue_name=queue_name       # In which queue the job should be put in
)

print scheduler.get_jobs()
