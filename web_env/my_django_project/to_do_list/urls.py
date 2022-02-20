from django.urls import include, re_path
# import views from local directory.
from . import views
urlpatterns = [
    # When user request home page http://localhost:8000/to_do, it will invoke the home function defined in views.py.
    re_path('', views.home, name='home'),
    # The first parameter is the url path.
    # The second parameter is the response function defined in views.py file. 
    # The third parameter is the url name which will be used in html file url tag.
    # For example, in html code {% url 'to_do_list:to_do_list' %} will be mapped to url http://localhost:8000/to_do/list_all
    re_path('list_all', views.to_do_list, name='to_do_list'),
    
    # <id> is a placeholder that will be replaced with the real record id.
    re_path('show_detail/<id>/', views.to_do_detail, name='to_do_detail'),
]