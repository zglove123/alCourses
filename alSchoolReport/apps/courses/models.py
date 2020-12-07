from django.db import models

# Create your models here.


class CourseInformation(models.Model):
    courseID = models.AutoField(primary_key=True, verbose_name="课程ID")
    courseName = models.CharField(max_length=20, verbose_name="课程名")

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.courseName


