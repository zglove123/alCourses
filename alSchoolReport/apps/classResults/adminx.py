import xadmin
from apps.classResults.models import ClassResult, UserClassInf

# 用户提示
from django.contrib import messages
from django.utils.translation import ngettext, _trans


# studentid = models.ForeignKey(StudentInformation, on_delete=models.CASCADE, verbose_name="学生ID")
# courseID = models.ForeignKey(CourseInformation, on_delete=models.CASCADE, verbose_name="课程ID")
# classscore = models.FloatField(max_length=6, default=0, verbose_name="成绩")
# class courseResAdmin(object):
#     list_display = ['studentid__username', 'courseID__courseName', 'classscore']
#     search_fields = ['studentid__username', 'courseID__courseName', 'classscore']
#     list_filter = ['studentid__username', 'courseID__courseName', 'classscore']
#     ordering = ['studentid', 'classscore']


class courseResAdmin(object):
    list_display = ['studentid', "getStuClass", "getStuGrade", 'courseID', 'classscore', 'add_time']
    # 因为search_fields中的项不是字符类型，例如字段类型是ForeignKey，则会报错
    search_fields = ['classscore']
    list_filter = ['courseID', 'classscore']
    # filter_horizontal = ['courseID', 'classscore', 'add_time']
    ordering = ['courseID', 'studentid']
    list_editable = ['classscore']
    actions = ['score_init']

    # 在Model OptionClass 中设定data_charts属性，该属性为dict类型，key是图表的标示名称，value是图表的具体设置属性，示例:
    # title : 图表的显示名称
    # x-field : 图表的 X 轴数据列, 一般是日期, 时间等
    # y-field : 图表的 Y 轴数据列, 该项是一个 list, 可以同时设定多个列, 这样多个列的数据会在同一个图表中显示
    # order : 排序信息, 如果不写则使用数据列表的排序
    # data_charts = {
    #     "user_count": {'title': u"成绩表格", "x-field": "add_time", "y-field": ("courseID",),
    #                    "order": ('add_time',)},
    #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    # }

    def getStuClass(self, obj):
        return obj.studentid.StudentClass
    getStuClass.short_description = "年级"  # 自定义字段的描述信息
    getStuClass.admin_order_field = "getStuClass"  # 自定义字段点击时使用哪个字段作为排序条件

    def getStuGrade(self, obj):
        return obj.studentid.StudentGrade
    getStuGrade.short_description = "班级"  # 自定义字段的描述信息
    getStuGrade.admin_order_field = "getStuGrade"  # 自定义字段点击时使用哪个字段作为排序条件

    # queryset 是包含了已经选择的数据的 queryset
    def score_init(self, request, queryset):
        rows_updated = queryset.update(classscore=0)
        if rows_updated == 1:
            message_bit = "一条"
        else:
            message_bit = "%s 条" % rows_updated
        messages.success(request, '%s 分数初始化已经完成.' % message_bit)  # 被忽略，不记录

    score_init.short_description = "分数初始化"  # 自定义字段的描述信息



    # def queryset(self):
    #     qs = super().queryset()
    #     if not self.request.user.is_superuser:
    #         qs = qs.filter(teacher=self.request.user.teacher)
    #     return qs
    # foreign_key__related_fieldname
    # user表格UserClassInf   相关联   通过user 获取USerClassiNf表的数据
    # class UserClassInf(models.Model):
    #     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="用户")
    #     StudentClass = models.ForeignKey(StudentClass, on_delete=models.CASCADE, null=True, blank=True,
    #                                      verbose_name="年级信息")
    #     StudentGrade = models.ForeignKey(StudentGrade, on_delete=models.CASCADE, null=True, blank=True,
    #                                      verbose_name="班级信息")
    #     classInformation = models.ForeignKey(CourseInformation, on_delete=models.CASCADE, null=True, blank=True,
    #                                          verbose_name="学科信息")
    # Cannot resolve keyword 'getStuClass' into field.
    # Choices are: add_time, classscore, courseID, courseID_id, id, studentid, studentid_id
    # 例如B中有一个 models.ForeignKey(A) 。而当我们需要反向查询 A 中某个具体实例所关联的 B 时，可能会用到 A.B_set.all() 或 B.objects.filter(A) 这两种不同的方法。
    # 例如BUserClassInf中有一个 models.ForeignKey(Auser) 。而当我们需要反向查询 Auser 中某个具体实例所关联的 BUserClassInf 时，
    # 可能会用到 A.B_set.all() 或 B.objects.filter(A) 这两种不同的方法。
    def queryset(self):
        qs = super().queryset()
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(
                           # courseID=UserClassInf.objects.filter(user=user).distinct('courseID'),
                           courseID=user.CourseInformation.courseID,
                           )
        return qs


class courseTeacherInfAdmin(object):
    list_display = ['user', "StudentClass", "StudentGrade", 'classInformation']
    search_fields = ['user', "StudentClass", "StudentGrade", 'classInformation']
    list_filter = ['user', "StudentClass", "StudentGrade", 'classInformation']
    ordering = [ "StudentClass", "StudentGrade", 'classInformation', 'user']
    list_editable = ["StudentClass", "StudentGrade", 'classInformation']


xadmin.site.register(ClassResult, courseResAdmin)
xadmin.site.register(UserClassInf, courseTeacherInfAdmin)



