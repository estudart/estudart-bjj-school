from celery import Celery

def make_celery():
    celery = Celery(
        "tasks",
        broker="redis://localhost:6379/0",
        backend="redis://localhost:6379/0",
        include=["services.celery.tasks"]
    )
    return celery

celery_service = make_celery()