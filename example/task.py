from celery import shared_task
from time import sleep
from django.core.mail import send_mail
import os

from celery.schedules import crontab


# from celery.decorators import periodic_task

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task(bind=True,
             name='send_email_task',
             max_retries=3,
             soft_time_limit=20)
def send_email_task(self):
    sleep(10)
    send_mail('funciono!',
              'prueba que funcionoooooooo',
              'gui.duquesanchez@gmail.com',
              ['gduque@activeit.cl'])
    return None


@shared_task(bind=True,
             name='hello_task',
             max_retries=3,
             soft_time_limit=20)
def hello_task(self):
    print('Hello')
    return None


@shared_task(bind=True,
             name='write_task',
             max_retries=3,
             soft_time_limit=20)
def write_task(self):
    save_path = 'C:/example/'
    name_of_file = 'text'
    complete_name = os.path.join(save_path, name_of_file + ".txt")
    with open(complete_name, "w") as file1:
        file1.write("blah blah blah")
