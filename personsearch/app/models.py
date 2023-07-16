from django.db import models


# Person -1to1-> Address
class State(models.TextChoices):
    NSW = 'NSW',
    VIC = 'VIC',
    QLD = 'QLD',


class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(
        max_length=3,
        choices=State.choices
    )


class Person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
