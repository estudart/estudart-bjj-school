from celery import Celery
from celery.schedules import crontab



def make_celery(app):
    celery = Celery(
        app.import_name, 
        broker=app.config['broker_url'],
        backend=app.config['result_backend'],
        include=["services.celery.tasks"])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask

    celery.conf.beat_schedule = {
        "run-my-task-every-10-seconds": {
            "task": "services.celery.tasks.check_and_send_reminders",
            "schedule": 10.0,  # Runs every 10 seconds
        },
    }
    return celery


# from celery import Celery
# from celery.schedules import crontab

# def make_celery(app):
#     celery = Celery(
#         app.import_name,
#         broker=app.config['CELERY_BROKER_URL'],
#         backend=app.config['CELERY_RESULT_BACKEND']
#     )
#     celery.conf.update(app.config)

#     celery.conf.beat_schedule = {
#         "check_and_send_reminders": {
#             "task": "services.celery.tasks.check_and_send_reminders",
#             "schedule": crontab(minute=0, hour=9),  # Run every day at 9 AM
#         },
#     }

#     return celery