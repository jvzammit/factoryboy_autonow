from datetime import datetime, time

from django.db import models
from django.utils import timezone


class OrderQueryset(models.QuerySet):
    def created_today(self):
        today_floor = datetime.combine(
            timezone.now(), time.min, tzinfo=timezone.get_current_timezone()
        )
        return self.filter(created_at__gte=today_floor)


class Order(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = OrderQueryset.as_manager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return str(self.id)
