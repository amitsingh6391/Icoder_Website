# Generated by Django 3.1.4 on 2020-12-02 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='timeStamp',
        ),
    ]
