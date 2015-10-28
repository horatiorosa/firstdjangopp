#configures what code is run when a request comes in based on the url path.
#we edit this files as new features are added
"""myfirstdjangopp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
MY NOTES
    URL function has 3 parameters
    the first param is REGEX and used to match the request
    the second param (arguement) is the view to call is there is a match
    the third param is a name param used in templates
"""
from django.conf.urls import url
from django.contrib import admin
from inventory import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
			# (?P...)	this is called a named group. This named group uses id in angle brackets to mean that the digit characters will be called id. when we use a named group, the part that matches will be passed to the view as a param
    url(r'^admin/', admin.site.urls),
]
