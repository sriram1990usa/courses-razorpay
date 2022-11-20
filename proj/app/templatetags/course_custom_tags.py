from django import template
import math
from proj.app.models.user_course import UserCourse
from proj.app.models.course import Course
register = template.Library()

@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount is 0:
        return price
    sellprice = price
    print('ln 12 ', type(sellprice))
    print('ln 13 ', type(price))
    print('ln 14 ', type(discount))
    sellprice = price-price*discount*0.01
    return math.floor(sellprice)


@register.filter
def rupee(price):
    return f'₹{price}'

@register.simple_tag
def is_enrolled(request, course):   
    user=None    
    if not request.user.is_authenticated:
        return False
    user=request.user
    try:
        user_course=UserCourse.objects.get(user=user, course=course)
        return True
    except:
        return False

