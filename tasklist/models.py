from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=55)
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField('date created')
#     updated_at = models.DateTimeField('last updated')
#     status = models.PositiveSmallIntegerField(default=1)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_head = models.CharField(max_length=200)
    parent_task_id = models.IntegerField(default=0)
    task_group = models.CharField(max_length=5, default='TASK')
    task_group_id = models.PositiveIntegerField(null=True)
    description = models.TextField(blank=True)
    due_date = models.DateField('due date')
    is_active = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(default=1)
    # def publish(self):
    #     self.pub_date = timezone.now()
    #     self.save()