import xadmin
from xadmin import views
from apps.students.models import StudentInformation, StudentGrade, StudentClass
# excel数据的导入和导出
from import_export import resources

"""
list_display 控制列表展示的字段
search_fields 控制可以通过搜索框搜索的字段名称，xadmin使用的是模糊查询
list_filter 可以进行过滤操作的列
ordering 默认排序的字段
readonly_fields 在编辑页面的只读字段
exclude 在编辑页面隐藏的字段
list_editable 在列表页可以快速直接编辑的字段
show_detail_fileds 在列表页提供快速显示详情信息
refresh_times 指定列表页的定时刷新
list_export 控制列表页导出数据的可选格式
show_bookmarks 控制是否显示书签功能
data_charts 控制显示图标的样式
model_icon 控制菜单的图标
"""


CLASS_INF = (("1", "一年级"), ("2", "二年级"), ("3", "三年级"),
            ("4", "四年级"), ("5", "五年级"), ("6", "六年级"),
            ("7", "七年级"), ("8", "八年级"), ("9", "九年级"))

GRADE_INF = (("1", "一班"), ("2", "二班"), ("3", "三班"),
            ("4", "四班"), ("5", "五班"), ("6", "六班"),
            ("7", "七班"), ("8", "八班"))


class StuInformation(resources.ModelResource):

    class Meta:
        model = StudentInformation
        fields = ('username', 'StudentClass', 'StudentGrade', 'gender', 'mobile')
        # exclude = ()

    def __unicode__(self):
        return self.username


class StudentInfAdmin(object):
    import_export_args = {'import_resource_class': StuInformation, 'export_resource_class': StuInformation}
    list_display = ['studentid', 'username', 'StudentClass', 'StudentGrade', 'gender', 'mobile']
    search_fields = ['studentid', 'username', 'StudentClass', 'StudentGrade', 'gender', 'mobile']
    list_filter = ['studentid', 'username', 'StudentClass', 'StudentGrade', 'gender', 'mobile']
    ordering = ['StudentClass', 'StudentGrade', 'username', 'studentid']
    list_per_page = 50


class StudentClassAdmin(object):
    list_display = ['classname']
    search_fields = ['classname']
    list_filter = ['classname']
    ordering = ['classname']


class StudentGradeAdmin(object):
    list_display = ['gradename']
    search_fields = ['gradename']
    list_filter = ['gradename']
    ordering = ['gradename']


xadmin.site.register(StudentInformation, StudentInfAdmin)
xadmin.site.register(StudentClass, StudentClassAdmin)
xadmin.site.register(StudentGrade, StudentGradeAdmin)
