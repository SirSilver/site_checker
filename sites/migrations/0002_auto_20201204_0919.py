from django.db import migrations
import pandas


def get_sites(apps, schema_editor):
    """Get list of sites from file and fill database"""
    Site = apps.get_model('sites', 'Site')
    sites = pandas.read_excel('Website-2020-12-03.xlsx')
    for url in sites.url:
        Site.objects.create(url=f'http://{url}', name=url)


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_sites),
    ]
