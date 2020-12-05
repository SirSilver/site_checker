import asyncio
from asgiref.sync import sync_to_async
from datetime import datetime
import socket
from celery import group, shared_task
import requests
from .models import Site, Status


@shared_task
def check_site(url):
    """Send HEAD request to `url` and create new Status object depend on response"""
    site = Site.objects.get(url=url)

    try:
        response = requests.head(url)
        code = response.status_code
        ip = socket.gethostbyname(site.name)
    except requests.ConnectionError:
        code = 503
        ip = None

    Status.objects.create(site=site, code=code, ip=ip)


@shared_task
def check_sites():
    """Get all Site objects and check their status"""
    sites = Site.objects.all()
    tasks = group([check_site.s(site.url) for site in sites])
    tasks.apply_async()
