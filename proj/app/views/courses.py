from cmath import log
from tkinter.messagebox import NO
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from proj.app.models.course import Course
from proj.app.models.user_course import UserCourse
from proj.app.models.video import Video
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator
# Create your views here.
   

def coursePage(request, slug):    
    course=Course.objects.get(slug=slug)
    print('ln 11 course: ', course) #ok
    serial_number=request.GET.get('lecture')
    print('ln 13 serial_number: ', serial_number) #None
    videos=course.video_set.all().order_by("serial_number")
    print('ln 15 videos: ', videos)  #ok
    
    next_lecture=2
      
    if serial_number is None:
        serial_number=1     
        prev_lecture=None
    else:
        next_lecture=int(serial_number)+1    
        prev_lecture=int(serial_number)-1
        if len(videos)<next_lecture:
            next_lecture=None
    
    video=Video.objects.get(serial_number=serial_number, course=course)
    print('ln 21 video: ', video)
    
    if (video.is_preview is False):   
        if(request.user.is_authenticated is False):
            return redirect('login')
        else:
            user=request.user
            try:
                user_course=UserCourse.objects.get(user=user, course=course)
            except:
                return redirect('check-out', slug=course.slug)

    context={
        'course':course,
        'videos':videos,
        'video':video,
        'next_lecture':next_lecture,
        'prev_lecture':prev_lecture        
    }
    return render(request, 'courses/course_page.html', context=context)#ok ok
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class MyCourseList(ListView):
    template_name='courses/my_courses.html'
    context_object_name='user_courses'

    def get_queryset(self):
        return UserCourse.objects.filter(user=self.request.user)
 
'''
@login_required(login_url='login')
def my_courses(request):
    user=request.user
    user_courses=UserCourse.objects.filter(user=user)
    print('ln 45 user_course ', user_courses)
    context={
        'user_courses':user_courses
    }
    return render(request=request, template_name='courses/my_courses.html', context=context)

'''
