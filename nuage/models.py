from django.db import models


class OwesandOwedBy(models.Model):
    name = models.TextField(max_length=255)
    owes = models.TextField(max_length=255)
    owed_by = models.TextField(max_length=255)
    balance = models.TextField(max_length=255)

    def __str__(self):
        return self.title
