from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_page, name="admins"),
    path('userlist',views.user_list,name='userlist')
]
