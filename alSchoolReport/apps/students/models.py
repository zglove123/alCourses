from django.db import models

GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)

CLASS_INF = (("1", "一年级"), ("2", "二年级"), ("3", "三年级"),
            ("4", "四年级"), ("5", "五年级"), ("6", "六年级"),
            ("7", "七年级"), ("8", "八年级"), ("9", "九年级"))

GRADE_INF = (("1", "一班"), ("2", "二班"), ("3", "三班"),
            ("4", "四班"), ("5", "五班"), ("6", "六班"),
            ("7", "七班"), ("8", "八班"))


# 需要新增年级表格
class StudentClass(models.Model):
    classname = models.CharField(max_length=10, verbose_name="年级", choices=CLASS_INF)

    class Meta:
        verbose_name = "学生年级"
        verbose_name_plural = verbose_name

    # 重写数据库表
    def __str__(self):
        return self.classname


# 需要新增年级表格
class StudentGrade(models.Model):
    gradename = models.CharField(max_length=10, verbose_name="年级", choices=GRADE_INF)

    class Meta:
        verbose_name = "学生班级"
        verbose_name_plural = verbose_name

    # 重写数据库表
    def __str__(self):
        return self.gradename


# 需要在setting中设置一下  这个是默认表，不在是之前的那张表了
class StudentInformation(models.Model):
    studentid = models.AutoField(primary_key=True, verbose_name="学号")
    username = models.CharField(max_length=50, verbose_name="学生姓名", unique=True, null=False, blank=False)
    StudentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE,  null=True, blank=True, verbose_name="年级信息")
    StudentGrade = models.ForeignKey(StudentGrade, on_delete=models.CASCADE,  null=True, blank=True, verbose_name="班级信息")
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    image = models.ImageField(verbose_name="学生头像", upload_to="head_image/%Y/%m", default="default.png")
    mobile = models.CharField(max_length=11, verbose_name="监护人手机号码")
    # mobile = models.CharField(max_length=11,unique=True,verbose_name="手机号码")

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    # # 读取未读消息数量
    # def unread_nums(self):
    # return self.usermessage_set.filter(has_read=False).count()

    # 重写数据库表
    def __str__(self):
        return self.username