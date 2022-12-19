import os
from celery import Celery
from .settings import EMAIL_HOST_USER

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orders.settings')

app = Celery('orders')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def send_confirm_mail(data):
    send_mail('Title', f'Заказ {data["name"]}\nсменил статус на "{data["status"]}"',
              EMAIL_HOST_USER, [data['email']], fail_silently=False)
