from django.urls import path
from .views import *

urlpatterns = [
    path('part', PartView.as_view()),
    path('category', CategoryView.as_view()),
    path('order', OrderView.as_view()),
]
