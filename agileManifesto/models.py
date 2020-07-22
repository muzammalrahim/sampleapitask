from django.db import models


class Value(models.Model):
    value = models.CharField(max_length=191, null=True, blank=True)

    def __str__(self):
        return self.value


class Principal(models.Model):
    principal = models.CharField(max_length=191, null=True, blank=True)

    def __str__(self):
        return self.principal
