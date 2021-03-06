"""sknase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


# View imports
from mainsite.views import main_page, o_nas, biblioteka, projekty, publikacje, recenzje, kontakt, rezerwacja

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page),
    url(r'^onas/$', o_nas),
    url(r'^biblioteka/$', biblioteka),
    url(r'^projekty/$', projekty),
    url(r'^publikacje/$', publikacje),
    url(r'^recenzje/$', recenzje),
    url(r'^kontakt/$', kontakt),
    url(r'^rezerwacja/$', rezerwacja),
    url(r'^tinymce/', include('tinymce.urls'))
]
