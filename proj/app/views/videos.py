from django.shortcuts import render
from django.shortcuts import HttpResponse
from proj.app.models.course import Course
# Create your views here.


def videoPage(request, slug):  
  
    course=Course.objects.get(slug=slug)
   
    videolist=course.video_set.all()
   
    vidtitle=course.video_set.filter(video_id='agICFVdcKk0') # ok ok
   
    context={
        'course':course,
        'vidtitle':vidtitle
    }
    return render(request, 'courses/course_page.html', context=context)#ok ok
   

