import xadmin
from apps.courses.models import CourseInformation


# @xadmin.site.register(CourseInformation)
class courseInfAdmin(object):
    list_display = ['courseID', 'courseName']
    search_fields = ['courseID', 'courseName']
    list_filter = ['courseID', 'courseName']
    ordering = ['courseID', 'courseName']


xadmin.site.register(CourseInformation, courseInfAdmin)



