from django.urls import path
from .views import Record, Login, Logout,RecordUpdate,List,update,DeleteUser

urlpatterns = [
    path('addUser/', Record.as_view(), name="register"),
    path('getuser/<str:pk>',RecordUpdate.as_view(),name="getUser"),
    path('updateuser/<str:pk>',update.as_view(),name='update'),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('list/',List.as_view(),name='list'),
    path('delete/<str:pk>',DeleteUser.as_view(),name='delete'),
    #path('seeRecord/',UserDetail.as_view(),name='seeRecord'),
]
