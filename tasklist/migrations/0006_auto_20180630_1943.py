# Generated by Django 2.0.6 on 2018-06-30 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0005_auto_20180630_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_description',
            new_name='description',
        ),
    ]
