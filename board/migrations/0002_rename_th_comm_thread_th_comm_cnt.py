# Generated by Django 3.2.4 on 2021-06-23 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='th_comm',
            new_name='th_comm_cnt',
        ),
    ]
