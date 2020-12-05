from django.db import models


class Site(models.Model):
    """Site model"""
    url = models.CharField('URL address', max_length=200)
    name = models.CharField('Site name', max_length=200)

    def __str__(self):
        return self.url


class Status(models.Model):
    """Site status response at some point of time"""
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name='statuses',
        related_query_name='status'
    )
    code = models.IntegerField('Status code')
    time = models.DateTimeField('Date and time of receiving status', auto_now_add=True)
    ip = models.GenericIPAddressField('IPv4 address', protocol='IPv4', blank=True, null=True)

    def __str__(self):
        return f'{self.site.url} - {self.code}'
