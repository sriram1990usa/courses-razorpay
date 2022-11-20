from django.contrib import admin
from proj.app.models.course import Course, CouponCode, Tag, Prerequisite, Learning
from proj.app.models.video import Video
from proj.app.models.user_course import UserCourse
from proj.app.models.payments import Payment
from django.utils.html import format_html

# Register your models here.
class TagAdmin(admin.TabularInline):
    model=Tag

class PrerequisiteAdmin(admin.TabularInline):
    model=Prerequisite

class LearningAdmin(admin.TabularInline):
    model=Learning

class VideoAdmin(admin.TabularInline):
#class VideoAdmin(admin.StackedInline):
    model=Video    

class CouponCodeAdmin(admin.TabularInline):
    model=CouponCode

class CourseAdmin(admin.ModelAdmin):
    inlines=[TagAdmin, PrerequisiteAdmin, LearningAdmin, VideoAdmin]
    #list_display=['name', 'price', 'discount', 'active']
    list_display=['name', 'get_price', 'get_discount', 'active']
    list_filter=('discount', 'active')

    def get_price(self, course):
        return f'₹ {course.price}'
    
    get_price.short_description='Price'

    def get_discount(self, course):
        return f'{course.discount} %'

    get_discount.short_description='Discount' 

class PaymentAdmin(admin.ModelAdmin):
    model=Payment
    list_display=['order_id', 'get_user', 'get_course', 'status']   
    list_filter=['status', 'course']

    def get_user(self, payment):
        return format_html(f"<a target='blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")
    get_user.short_description='User' 

    def get_course(self, payment):
        return format_html(f"<a target='blank' href='/admin/app/course/{payment.course.id}'>{payment.course}</a>")
    get_course.short_description='Course' 

class UserCourseAdminModel(admin.ModelAdmin):
    model=UserCourse
    list_display=['click','get_user', 'get_course']   
    list_filter=['user', 'course']

    def click(self, usercourse):
        return "Click to Open"
        
    def get_user(self, usercourse):
        return format_html(f"<a target='blank' href='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</a>")
    get_user.short_description='User' 

    def get_course(self, usercourse):
        return format_html(f"<a target='blank' href='/admin/app/course/{usercourse.course.id}'>{usercourse.course}</a>")
    get_course.short_description='Course' 

admin.site.register(Course, CourseAdmin)
admin.site.register(CouponCode)
admin.site.register(Video)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserCourse, UserCourseAdminModel)
