from django.contrib import admin
from django.urls import path
from home.views import home_view, var_view, nums_view
#from home.views import home_view
#from home.views import var_view
#from home.views import nums_view
from todo.views import todo_view, todo_inprogress_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('var/',var_view),
    path('nums/', nums_view),
    path("todos/", todo_view, name="todos"),
    path("todos/in_progress", todo_inprogress_view, name="todos")
    ]
