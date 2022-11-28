from celery import shared_task
from django.core.mail import send_mail
from .models import Post, Category
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


@shared_task
def subscribers_new_post():
    new_post = Post()
    send_mail(
        subject="You have new posts in subscriptions",
        message=new_post.post_text[:50],
        from_email=os.environ.get('EMAIL') + 'yandex.ru',
        recipient_list=Category.category_subscribers
    )
