
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='index'),
    path('add/',views.ADD,name='add'),
    path('<int:id>',views.EDIT,name='edit'),
    path('delete<str:id>',views.DELETE,name='delete'),
]

