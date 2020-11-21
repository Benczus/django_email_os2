from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return


@shared_task
def test_mail_send(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
    return