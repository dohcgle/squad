from django.db import models

class Power(models.Model):
    item = models.CharField(max_length=150)

    def __str__(self):
        return self.item

class Members(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    secretIdentity = models.CharField(max_length=150)
    powers = models.ManyToManyField(Power)


    def __str__(self):
        return self.name


class Squad(models.Model):
    squadName = models.CharField(max_length=150)
    homeTown = models.CharField(max_length=150)
    formed = models.IntegerField()
    secretBase = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    members = models.ForeignKey(Members, related_name='related_members', on_delete=models.CASCADE)

    def __str__(self):
        return self.squadName
