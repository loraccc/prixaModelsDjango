from django.db import models
from datetime import datetime
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
# from autoslug import AutoSlugField
# Create your models here.

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

class Unmanaged(models.Model):
    class Meta:
        abstract = True
        # managed = False

# this is subclassing the meta data by inheriting commonInfo
    class meta(CommonInfo.Meta):
        db_table = "student_info"


# what this does is it inherits abstract method from commonInfo and also inherits managed=false from unmanaged model 
class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    # class Meta(CommonInfo.Meta, Unmanaged.Meta):
    #     pass


# class CommonInfoWithTimestamp(CommonInfo):
#     timestamp = models.DateTimeField(default=datetime.now)

#     class Meta:
#         proxy = True

# ---------------MODEL

#  WHAT MODEL MANAGER DOES IS THAT IT HELPS RETRIEVE A SET OF QUERIES FORM ANY MODEL ACCORDING TO NEED AND NOT example.objects.all()


class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    # ... other fields ...

    def save(self, *args, **kwargs):
        # Set end_date to start_date + 3 months
        self.end_date = self.start_date + timezone.timedelta(days=3 * 30)  # Assuming approximately 30 days per month
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='lesson_thumbnails/')
    file = models.FileField(upload_to='lesson_files/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'mp3', 'mp4'])])
    slug = models.SlugField(unique=True, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        # Auto-generate the slug when saving the lesson
        if not self.slug:
            print(self.id,'iddddddddddddddddddd')
            self.slug=slugify(self.title + str(self.id) )
                # raise Exception("Error creating slug")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
