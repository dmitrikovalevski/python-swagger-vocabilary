from django.db import models


class Card(models.Model):
    english = models.CharField(max_length=200)
    russian = models.CharField(max_length=200)
    new_card = models.BooleanField(null=True)
    remembered = models.BooleanField(null=False)
    part_of_speech = models.CharField(max_length=200)
    repeat = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.russian} - {self.english}'
