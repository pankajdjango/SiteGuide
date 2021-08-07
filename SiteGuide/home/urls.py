from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('add',views.add_user,name='add'),
    path('edit/<int:id>/',views.edit_Patient,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),

]
