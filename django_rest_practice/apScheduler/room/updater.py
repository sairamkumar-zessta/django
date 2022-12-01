from apscheduler.schedulers.background import BackgroundScheduler
from .something_update import create_object


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(create_object, 'interval', seconds=10)
    scheduler.start()