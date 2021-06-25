from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="home-page"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.destroy, name='delete'),    
]