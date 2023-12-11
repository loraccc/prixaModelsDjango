from django.db import models
from datetime import datetime

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        # manage=False means that commonInfo table will not be created in the databsse

    def __str__(self) -> str:
        return self.name

# CommonInfo is the name of class thats inherited from above
class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False

# this is subclassing the meta data by inheriting commonInfo
    class Meta(CommonInfo.Meta):
        db_table = "student_info"


# what this does is it inherits abstract method from commonInfo and also inherits managed=false from unmanaged model 
class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass


# class CommonInfoWithTimestamp(CommonInfo):
#     timestamp = models.DateTimeField(default=datetime.now)

#     class Meta:
#         proxy = True