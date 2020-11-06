from django.urls import path
from .views import HomePageView
from .views import WordView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('words/', WordView.as_view()),
    path('words/<int:pk>', WordView.as_view()),
]
