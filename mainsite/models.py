# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class author(models.Model):
	first_name = models.CharField(max_length=30)
	second_name = models.CharField(max_length=30, blank = True)
	last_name = models.CharField(max_length=30)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class publisher(models.Model):
	name = models.CharField(max_length=60)
	address = models.CharField(max_length=50, blank = True)
	website = models.URLField(blank = True)

	def __unicode__(self):
		return self.name

class subject(models.Model):
	subject = models.CharField(max_length=100)

	def __unicode__(self):
		return self.subject

class book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(author)
	publisher = models.ForeignKey(publisher)
	pages = models.PositiveIntegerField()
	tags = models.ManyToManyField(subject)
	description = models.TextField()

	def __unicode__(self):
		return self.title

class user(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()
	is_a_member = models.BooleanField()
	phone_number = models.CharField(max_length=9, blank = True)

	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class status(models.Model):
	status = models.CharField(max_length=20)

	def __unicode__(self):
		return self.status

class order(models.Model):
	book = models.ForeignKey(book)
	user = models.ForeignKey(user)
	order_date = models.DateField(auto_now_add = True)
	due = models.DateField()
	status = models.ForeignKey(status)

	def __unicode__(self):
		return u'%s %s %s %s' % (self.book, self.user, self.due, self.status)