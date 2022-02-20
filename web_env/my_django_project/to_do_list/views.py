from django.shortcuts import render
# Import ToDo model class defined in current models.py file.
from .models import ToDo
import os
# Calculate django application execute directory path.
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
# This function will return and render the home page when url is http://localhost:8000/to_do/.
def home(request):
    # Get the index template file absolute path.
    index_file_path = PROJECT_PATH + '/pages/home.html'
    # Return the index file to client.
    return render(request, index_file_path)
# This function will display todos in a list page the request url is http://localhost:8000/to_do/list_all.
def to_do_list(request):
    # Get all todos model object order by handle_date column.
    todos = ToDo.objects.order_by('handle_date')
    # Add the todos list in Django context.
    context = {'todos' : todos}
    # Get the list page absolute path. 
    to_do_list_file_path = PROJECT_PATH + '/pages/list.html'
    # Render and return to the list page.
    return render(request, to_do_list_file_path, context)
# Display the todo detail information in web page. The input parameter is todo id. The request url is http://localhost:8000/to_do/show_detail/3/.
def to_do_detail(request, id):
    # Get todo object by id.
    todo = ToDo.objects.get(id=id)
    # Set the todo object in context.
    context = {'todo' : todo}
    # Get todo detail page absolute file path.
    to_do_detail_file_path = PROJECT_PATH + '/pages/detail.html'
    # Return the todo detail page.
    return render(request, to_do_detail_file_path, context)