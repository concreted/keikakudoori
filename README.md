# keikakudoori

## start

Starting the base stack (RabbitMQ/Redis/Celery app):
```
rabbitmq-server
redis-server
source bin/activate
TZ=UTC PYTHONPATH=src celery -A tasks worker --loglevel=info
```

Testing the base stack:
```
TZ=UTC PYTHONPATH=src python -i manual.py
```

Starting the scheduler (Redbeat):
```
TZ=UTC PYTHONPATH=src celery -A tasks beat -S redbeat.RedBeatScheduler
```
