from django.db import models


class Task(models.Model):
    text = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.text