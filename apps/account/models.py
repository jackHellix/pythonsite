from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255, unique=True)
    secondName = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email, self.firstName, self.secondName

    class Meta:
        ordering = ('-created_at', )
