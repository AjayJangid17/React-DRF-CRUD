# Generated by Django 2.2.4 on 2020-07-23 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200723_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='one_click_purchasing',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='stripe_customer_id',
        ),
    ]
