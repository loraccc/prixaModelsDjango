from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

# CommonInfo is the name of class thats inherited from above
class Student(CommonInfo):  
    home_group = models.CharField(max_length=5)
# this is subclassing the meta data by inheriting commonInfo
    class Meta(CommonInfo.Meta):
        db_table = "student_info"