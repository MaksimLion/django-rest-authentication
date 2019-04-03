from django.urls import path
from . import views


urlpatterns = [
    path('auth/', views.HelloView.as_view()),

]
