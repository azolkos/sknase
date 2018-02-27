from django import template

from mainsite.models import order
import datetime

register = template.Library()

@register.filter(name='getStatus')
def getStatus(id):
    o = order.objects.all().filter(book_id=id)
    if not o:
        return "Available"
    else:
        oa = o.filter(status=5)
        if oa:
            return 5
        else:
            return 4


@register.filter(name='dueDate')
def dueDate(id):
    o = order.objects.all().filter(book_id=id)
    if not o:
        return datetime.date.today()
    else:
        return o.get(status=5).due
