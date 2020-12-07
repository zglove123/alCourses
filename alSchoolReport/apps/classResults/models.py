from django.db import models

from apps.users.models import BaseModel

from apps.students.models import StudentInformation, StudentClass, StudentGrade
from apps.courses.models import CourseInformation
from django.contrib.auth.models import User


# Create your models here.


class ClassResult(BaseModel):
    studentid = models.ForeignKey(StudentInformation, on_delete=models.CASCADE, verbose_name="学生")
    courseID = models.ForeignKey(CourseInformation, on_delete=models.CASCADE, verbose_name="课程")
    classscore = models.FloatField(max_length=6, default=0, verbose_name="成绩")

    class Meta:
        verbose_name = "课程成绩信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{username}同学的{courseName}成绩为{score}".format(username=self.studentid.username, courseName=self.courseID.courseName, score=self.classscore)


class UserClassInf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  verbose_name="用户")
    StudentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE, null=True, blank=True, verbose_name="年级信息")
    StudentGrade = models.ForeignKey(StudentGrade, on_delete=models.CASCADE, null=True, blank=True, verbose_name="班级信息")
    classInformation = models.ForeignKey(CourseInformation, on_delete=models.CASCADE, null=True, blank=True, verbose_name="学科信息")

    class Meta:
        verbose_name = "教师班级信息"
        verbose_name_plural = verbose_name

    # 重写数据库表
    def __str__(self):
        return "{username}老师的{classInformation}学科已增加".format(username=self.user, classInformation=self.classInformation)