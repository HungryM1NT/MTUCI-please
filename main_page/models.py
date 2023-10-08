from django.db import models


class Person(models.Model):
    photo = models.ImageField(upload_to='persons_images')
    surname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'