from django import template

from mainsite.models import book, order

register = template.Library()

@register.filter(name='getStatus')
def getStatus(id):
	o = order.objects.all()
	try:
		return o.get(book_id=id).status_id
	except:
		return "Available"

@register.filter(name='dueDate')
def dueDate(id):
	o = order.objects.all()
	try:
		return o.get(book_id=id).due
	except:
		return now()
