from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from proj.app.models.course import Course, CouponCode
from proj.app.models.payments import Payment
from proj.app.models.user_course import UserCourse
from proj.app.models.video import Video
from proj.settings import *
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import razorpay
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))

# Create your views here.
@login_required(login_url='/login')
def checkout(request, slug):
    course=Course.objects.get(slug=slug)   
    user=request.user
    #if not request.user.is_authenticated:
    #    return redirect('login')        
    action=request.GET.get('action')    
    couponcode=request.GET.get('couponcode')
    coupon_code_message=None
    coupon=None
    order=None
    payment=None
    error=None
    try:
        user_course=UserCourse.objects.get(user=user, course=course)
        error="You are already enrolled in this course"
    except:
        pass   
    amount=None

 
    if error is None:
        amount=int(course.price-(course.price*course.discount*0.01))*100
   
    if couponcode:
        try:
            coupon=CouponCode.objects.get(course=course, code=couponcode)
            amount=course.price-(course.price*coupon.discount*0.01)
            amount=int(amount)*100
            print('ln 44 checkout.py amount ', amount)
        except:
            print('coupon code invalid')
            coupon_code_message="coupon code invalid"

   
    if amount==0:
        userCourse=UserCourse(user=user, course=course)
        userCourse.save()   
        #return HttpResponse('enrolled free')
        return redirect('my-courses')
    
    
    if action=='create_payment': 
        currency="INR"
        receipt=f"proj.{time()}"
        notes= {
            'email':user.email,
            #'name':f'{user.first_name} {user.last_name}'
            'name':f'{user.username}'  
        }   
        order=client.order.create({
                "amount": amount,
                "currency": currency,
                "receipt": receipt,
                "notes": notes   
            })
        payment=Payment()
        payment.user=user
        payment.course=course
        payment.order_id=order.get('id')
        payment.save()
        print('ln 77 payment ', payment)
    
    
    context={
        'course':course,
        'order':order,
        'payment':payment,
        'user':user,
        'error':error,
        'coupon':coupon,
        'coupon_code_message':coupon_code_message
    }
    return render(request, 'courses/checkout.html', context=context)#ok ok

@csrf_exempt
def verifyPayment(request):
    if request.method=='POST':
        data=request.POST
        print('ln 56 data ', data)
        context={}
        try:           
            client.utility.verify_payment_signature(data)
            print('ln 60 data: ', data)  # ok
           
            razorpay_order_id=data.get('razorpay_order_id')
            razorpay_payment_id=data.get('razorpay_payment_id')
            

            payment=Payment.objects.get(order_id=razorpay_order_id)
            print('ln 67 payment: ', payment)
            payment.payment_id=razorpay_payment_id
            payment.status=True

            userCourse=UserCourse(user=payment.user, course=payment.course)
            userCourse.save()
            print('ln 73 userCourse: ', userCourse)
            print('ln 74 userCourse.id: ', userCourse.id)

            payment.user_course=userCourse
            payment.save()

            return redirect('my-courses')

        except:           
            print('invalid payment request')
            return HttpResponse('invalid payment request from verifyPayment in checkout.py')
