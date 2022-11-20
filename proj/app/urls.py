from django.urls import path
from proj.app.views import HomePageView, SignupView, LoginView, signout, checkout
from proj.app.views.courses import coursePage, MyCourseList
from proj.app.views.checkout import verifyPayment
from proj.app.views.videos import videoPage
from django.conf.urls.static import static
from django.conf import settings
from django.views import View
'''
def home(request):
    return HttpResponse('from app url.py')
'''  
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup', SignupView.as_view(), name='signup'),    
    path('login', LoginView.as_view(), name='login'),
    path('logout', signout, name='logout'),   
    path('check-out/logout', signout, name='logout'), 
    path('course/logout', signout, name='logout'), 
    path('check-out/<str:slug>', checkout, name='check-out'),
    path('verify_payment', verifyPayment, name='verify_payment'),
    path('course/<str:slug>', coursePage, name='coursepage'),
    path('video/<str:slug>', videoPage, name='videopage'),
    path('my-courses', MyCourseList.as_view(), name='my-courses')
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)