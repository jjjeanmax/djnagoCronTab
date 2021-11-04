from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=255)


class Document(models.Model):
    upload_file = models.FileField(upload_to='files/')
    expiration_date = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
