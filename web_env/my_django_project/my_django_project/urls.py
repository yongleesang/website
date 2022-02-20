"""my_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, re_path

urlpatterns = [
    # When request http://localhost:8000/admin/, it will use url mappings defined in admin.site.urls.py file
    re_path('admin/', admin.site.urls),
    # When request http://localhost:8000/to_do, it will use url mappings defined in to_do_list.urls.py file
    # The include function must contains a tuple and a namespace key value pair. 
    # The tuple first element is the app urls mapping file, the second element is the application name.
    # If do not provide the application name, it will throw Specifying a namespace in include() without providing an app_name is not supported error.
    re_path('to_do/', include(('to_do_list.urls','to_do_list'), namespace='to_do_list')),
    re_path('polls/', include('polls.urls')),
    re_path('', include('resumesite.urls'))
]
