from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    unit = models.IntegerField(default=0)

    question1 = models.CharField(max_length=1000)
    answer1 = models.CharField(max_length=1000)

    question2 = models.CharField(max_length=1000)
    answer2 = models.CharField(max_length=1000)

    question3 = models.CharField(max_length=1000)
    answer3 = models.CharField(max_length=1000)

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + self.name + '(' + str(self.unit) + ')>'