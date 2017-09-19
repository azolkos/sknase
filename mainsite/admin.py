# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mainsite.models import author, publisher, subject, book, user, status, order, orderHistory
# Register your models here.

class bookAdmin(admin.ModelAdmin):
	list_filter = ('authors', 'tags')
	filter_horizontal = ('authors', 'tags')

class orderAdmin(admin.ModelAdmin):
	list_display = ('book', 'user', 'order_date', 'due', 'status')

class orderHistoryAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'order_date', 'due', 'overdue')

admin.site.register(author)
admin.site.register(publisher)
admin.site.register(subject)
admin.site.register(book, bookAdmin)
admin.site.register(user)
admin.site.register(status)
admin.site.register(order, orderAdmin)
admin.site.register(orderHistory, orderHistoryAdmin)
