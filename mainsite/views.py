# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render
from mainsite.models import book, author, publisher, subject, order, user, status
from mainsite.forms import orderForm, contactForm

import datetime

import os
# Create your views here.
def main_page(request):
	files = os.listdir("static/img/slider")
	fileCount = range(len(files))
	firstItem = files[0]
	return render(request, 'mainPage.html', locals())

def o_nas(request):
	return render(request, 'onas.html')

def biblioteka(request):
	b = book.objects.all().order_by('title')
	u = user.objects.all()

	if request.method == 'POST':
		form = orderForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			book_id = request.POST.get('book_id', None)
			bookItem = b.get(id=book_id)
			now = datetime.date.today()
			dueDate = now + datetime.timedelta(days=21)
			statusItem = status.objects.get(id=4)
			try:
				client = u.get(email=cd.get('email'))
				try:
					order.objects.get(user_id=client.id)
					request.session["regerror"] = 1
				except:
					newOrder = order(book=bookItem, user=client, order_date=now, due=dueDate, status=statusItem)
					newOrder.save()
					request.session["regerror"] = 0
			except:
				newUser = user(first_name=cd.get('name').capitalize(), last_name=cd.get('surname').capitalize(), email=cd.get('email'), is_a_member=False, phone_number=cd.get('phone'))
				newUser.save()
				client = u.get(email=cd.get('email'))
				newOrder = order(book=bookItem, user=client, order_date=now, due=dueDate, status=statusItem)
				newOrder.save()
				request.session["regerror"] = 0
			return HttpResponseRedirect('/rezerwacja/')
	else:
		form = orderForm()

	return render(request, 'biblioteka.html', locals())

def projekty(request):
	return render(request, 'projekty.html')

def recenzje(request):
	return render(request, 'recenzje.html')

def kontakt(request):
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print "cos"
	else:
		form = contactForm()
	return render(request, 'kontakt.html', locals())

def rezerwacja(request):
	if "regerror" in request.session:
		error = request.session["regerror"]
	else:
		error = None
	return render(request, 'rezerwacja.html', locals())