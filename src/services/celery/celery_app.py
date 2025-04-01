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

    number_of_minutes = 1

    # celery.conf.beat_schedule = {
    #     "run-my-task-every-5-minutes": {
    #         "task": "services.celery.tasks.check_and_send_reminders",
    #         "schedule": 60.0 * number_of_minutes,  # Runs every x minutes
    #     },
    # }

    return celery
