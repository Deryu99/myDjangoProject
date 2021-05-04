"""myDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

""" 
    Map URLs to certain locations 
    - When we go to '.../todoList' it gets mapped to 'todoList.urls' 
    - When Django matches a path pattern it chops off the matched part and sends remaining string to the included urls module for further processing
    - '' (empty path) is also homepage
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoList.urls')),
    path('index/', include('todoList.urls'))
]

"""path('todoList/', include('todoList.urls'))"""