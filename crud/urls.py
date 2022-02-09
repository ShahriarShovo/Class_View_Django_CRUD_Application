from django.urls import path
from crud import views

app_name='crud'

urlpatterns = [
   path('', views.Index.as_view(), name='index' ),
   path('add/', views.Add_employee.as_view(), name='add'),
   path('update/<pk>/', views.Update_employee.as_view(), name='update'),
   path('delete/<pk>/', views.Delete.as_view(), name='delete')
]
