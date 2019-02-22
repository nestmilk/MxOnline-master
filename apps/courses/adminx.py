# _*_ coding: utf-8 _*_
import xadmin

__author__ = 'nestmilk'
__date__ = '2019/1/13 23:25'

from .models import Course, Lesson, Video, CourseResource, BannerCourse


class LessonInline(object):
    model = Lesson
    extra = 0

class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name','course_org','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','category', 'tag','get_zj_nums','go_to', 'add_time']
    search_fields = ['name','course_org','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','category', 'tag']
    list_filter = ['name','course_org','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','category', 'tag','add_time']
    inlines = [LessonInline, CourseResourceInline]
    style_fields = {"detail":"ueditor"}
    import_excel = True

    #刷新时间页面
    # refresh_times = [3, 5]

    def save_models(self):
        #在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)



class BannerCourseAdmin(object):
    list_display = ['name','course_org','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','category', 'tag', 'add_time']
    search_fields = ['name','course_org','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','category', 'tag']
    list_filter = ['name','course_org','desc','detail','degree','learn_times','students','fav_nums','image','click_nums','category', 'tag','add_time']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields =['course', 'name', 'download']
    list_filter =['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)

xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)