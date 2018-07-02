# Generated by Django 2.0.6 on 2018-06-24 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(verbose_name='last updated')),
                ('status', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tasklist.User'),
            preserve_default=False,
        ),
    ]
